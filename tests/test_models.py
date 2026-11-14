"""
AnalogX — Planetary Analog Discovery Engine
Suite de Pruebas Unitarias para Modelos Pydantic y Catálogo de Datos
Compatible con unittest y pytest.
"""

import csv
import os
import sys
import unittest
from pydantic import ValidationError

# Asegurar que el backend esté en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.models.dataset import (
    AccessTypeEnum,
    DatasetMetadata,
    PriorityEnum,
    ProcessingComplexityEnum,
    ScientificSource,
    StrictCategoryEnum,
    VerificationStatusEnum,
)
from app.models.evidence import (
    ComparabilityTypeEnum,
    QualitativeEvidence,
    ScientificLimitation,
    StructuredComparison,
)
from app.models.observation import (
    ObservationMeasurement,
    ObservedVariable,
)
from app.models.region import (
    BoundingBox,
    CoordinateSystemTypeEnum,
    CRSDatumMetadata,
    PlanetEnum,
    PlanetaryRegion,
    TerrestrialRegion,
)


class TestAnalogXModels(unittest.TestCase):
    """Pruebas unitarias de validación e invariantes para AnalogX Backend."""

    def test_scientific_source_creation(self):
        """Valida la creación de una fuente científica oficial con metadatos reales."""
        source = ScientificSource(
            id="nasa_pds",
            name="NASA Planetary Data System",
            agency="NASA",
            catalog_or_mission="Geosciences Node / Imaging Node",
            url="https://pds.nasa.gov/",
            access_type=AccessTypeEnum.publico_sin_login,
            license="NASA Open Data Policy",
            verification_status=VerificationStatusEnum.verificado_con_fuente,
            priority=PriorityEnum.MVP,
            notes="Acceso libre por ODE REST API y HTTPS directo",
        )
        self.assertEqual(source.id, "nasa_pds")
        self.assertEqual(source.access_type, AccessTypeEnum.publico_sin_login)
        self.assertEqual(source.verification_status, VerificationStatusEnum.verificado_con_fuente)

    def test_terrestrial_region_uyuni(self):
        """Valida el esquema de la región terrestre de calibración (Salar de Uyuni)."""
        wgs84 = CRSDatumMetadata(
            crs_name="WGS 84 / Geographic",
            crs_code="EPSG:4326",
            datum_name="World Geodetic System 1984",
            reference_surface="Geoide EGM96",
            is_planetary=False,
        )
        bbox = BoundingBox(
            min_lat=-20.80,
            max_lat=-19.80,
            min_lon=-68.10,
            max_lon=-67.10,
            crs_code="EPSG:4326",
        )
        uyuni = TerrestrialRegion(
            id="bo_salar_uyuni",
            name="Salar de Uyuni",
            country="Bolivia",
            department="Potosí / Oruro",
            bounding_box=bbox,
            center_lat=-20.25,
            center_lon=-67.60,
            elevation_min_m=3653.0,
            elevation_max_m=3660.0,
            crs_datum=wgs84,
            geological_context="Cuenca evaporítica hiperplana endorreica",
            is_reference_site=True,
            primary_evaporite_minerals=["Halita", "Yeso", "Ulexita"],
            literature_references=["NASA Earth Observatory (2022)"],
        )
        self.assertTrue(uyuni.is_reference_site)
        self.assertEqual(uyuni.bounding_box.min_lat, -20.80)
        self.assertFalse(uyuni.crs_datum.is_planetary)

    def test_planetary_region_terra_sirenum(self):
        """Valida el esquema del objetivo marciano candidato con Areoide MOLA."""
        mars_datum = CRSDatumMetadata(
            crs_name="IAU 2000 Mars / Planetocentric",
            crs_code="IAU:49900",
            datum_name="Mars 2000",
            reference_surface="Areoide MOLA (R=3396.0 km)",
            is_planetary=True,
            equatorial_radius_m=3396190.0,
        )
        sirenum = PlanetaryRegion(
            id="mars_terra_sirenum_01",
            planet=PlanetEnum.Marte,
            target_feature_name="Depósito de cloruro de Terra Sirenum",
            regional_context="Tierras altas del sur de Marte",
            center_lat=-38.80,
            center_lon=221.00,
            coordinate_system_type=CoordinateSystemTypeEnum.planetocentrico,
            crs_datum=mars_datum,
            target_type="deposito_cloruros",
            primary_references=["Osterloo et al. (2010) JGR"],
            known_instrumental_observations=["PSP_003160_1410", "THEMIS DCS B8-7-5"],
        )
        self.assertEqual(sirenum.planet, PlanetEnum.Marte)
        self.assertEqual(sirenum.center_lat, -38.80)
        self.assertTrue(sirenum.crs_datum.is_planetary)

    def test_observation_measurement_13_fields(self):
        """
        Verifica que ObservationMeasurement cumpla rigurosamente con los 13 campos obligatorios
        y admita valores None/Optional en campos pendientes de verificación.
        """
        # 1. Medición instrumental verificada con valor numérico
        obs1 = ObservationMeasurement(
            id="obs_mola_meg128_slope_sirenum",
            source_name="NASA PDS Geosciences Node",
            source_url="https://pds-geosciences.wustl.edu/missions/mgs/mola.html",
            product_id="MOLA_MEGDR_MEG128",
            acquisition_date="2001-05-15",
            version="1.0",
            unit="grados",
            spatial_resolution="463m",
            crs_datum="Areoide MOLA / IAU 2000 Planetocentric",
            processing_method="Derivación de gradiente de elevación en ventana 3x3",
            value=0.78,
            quality_uncertainty="Desviación típica ±0.15° a escala de celda de 463m",
            verification_status=VerificationStatusEnum.verificado_con_fuente,
        )
        self.assertEqual(obs1.id, "obs_mola_meg128_slope_sirenum")
        self.assertEqual(obs1.value, 0.78)
        self.assertEqual(obs1.verification_status, VerificationStatusEnum.verificado_con_fuente)

        # 2. Medición con campos pendientes de verificar (sin inventar datos)
        obs2 = ObservationMeasurement(
            id="obs_sol_de_manana_flux_pending",
            source_name="NASA Earthdata / ASTER",
            source_url="https://search.earthdata.nasa.gov/",
            product_id="ASTER_GED_V003",
            acquisition_date=None,
            version=None,
            unit="W/m²",
            spatial_resolution="100m",
            crs_datum="WGS84 / EGM96",
            processing_method="Modelado de flujo de calor geotermal",
            value=None,  # No inventado; explícitamente None
            quality_uncertainty=None,
            verification_status=VerificationStatusEnum.pendiente_de_verificar,
        )
        self.assertIsNone(obs2.value)
        self.assertIsNone(obs2.acquisition_date)
        self.assertEqual(obs2.verification_status, VerificationStatusEnum.pendiente_de_verificar)

    def test_structured_comparison_and_limitations(self):
        """Valida la comparación estructurada y la documentación de limitaciones físicas."""
        limitation = ScientificLimitation(
            id="lim_gravity_01",
            parameter_name="Gravedad superficial",
            terrestrial_condition="g = 9.81 m/s²",
            planetary_condition="g = 3.71 m/s²",
            limitation_mechanism="Menor gravedad en Marte permite taludes clásticos estables con pendientes mayores",
            impact_on_analogy="No afecta fondos de cuenca horizontales hidrostáticos",
            is_blocking_for_direct_comparison=False,
        )

        comp = StructuredComparison(
            id="comp_slope_uyuni_sirenum",
            terrestrial_region_id="bo_salar_uyuni",
            planetary_region_id="mars_terra_sirenum_01",
            variable_or_feature="Pendiente de fondo de cuenca",
            comparability_type=ComparabilityTypeEnum.directa,
            terrestrial_measurement_id="obs_nasadem_slope_uyuni",
            planetary_measurement_id="obs_mola_meg128_slope_sirenum",
            resolution_compatibility="Requiere remuestreo: 30m terrestre vs 463m marciano",
            resampling_required=True,
            physical_divergence_notes="Pendientes de borde de cuenca concordantes con límites de sedimentación",
            scientific_limitations=[limitation],
            verification_status=VerificationStatusEnum.verificado_con_fuente,
            summary_conclusion="Alta plausibilidad morfométrica.",
        )
        self.assertEqual(comp.comparability_type, ComparabilityTypeEnum.directa)
        self.assertTrue(comp.resampling_required)
        self.assertEqual(len(comp.scientific_limitations), 1)
        self.assertFalse(comp.scientific_limitations[0].is_blocking_for_direct_comparison)

    def test_csv_dataset_catalog_integrity(self):
        """
        Lee el archivo CSV oficial 'research/dataset_catalog.csv' y verifica que
        cada fila cumpla con los campos obligatorios y la categoría estricta.
        """
        csv_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "research", "dataset_catalog.csv")
        )
        self.assertTrue(os.path.exists(csv_path), f"El archivo no existe: {csv_path}")

        valid_strict_categories = {
            StrictCategoryEnum.dato_instrumental.value,
            StrictCategoryEnum.producto_derivado.value,
            StrictCategoryEnum.interpretacion_bibliografica.value,
            StrictCategoryEnum.dato_demostracion.value,
        }

        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        self.assertGreaterEqual(len(rows), 10, f"Se esperaban al menos 10 datasets, se encontraron {len(rows)}")

        for i, row in enumerate(rows, start=1):
            self.assertTrue(row["identificador_oficial"], f"Fila {i} sin identificador_oficial")
            self.assertTrue(row["enlace"].startswith("http"), f"Fila {i} con enlace inválido: {row['enlace']}")
            self.assertTrue(row["resolucion"], f"Fila {i} sin resolución")
            self.assertTrue(row["unidades"], f"Fila {i} sin unidades")
            cat = row["categoria_estricta"]
            self.assertIn(
                cat,
                valid_strict_categories,
                f"Fila {i} con categoria_estricta inválida '{cat}'. Debe ser una de {valid_strict_categories}",
            )

    def test_validation_error_on_invalid_enum(self):
        """Verifica que Pydantic rechace valores no permitidos en enums estrictos."""
        with self.assertRaises(ValidationError):
            ObservationMeasurement(
                id="bad_obs",
                source_name="Unknown",
                source_url="https://invalid.org",
                product_id="TEST",
                unit="m",
                spatial_resolution="10m",
                crs_datum="WGS84",
                processing_method="None",
                verification_status="ESTADO_INVENTADO",  # Debe fallar
            )


if __name__ == "__main__":
    unittest.main()
