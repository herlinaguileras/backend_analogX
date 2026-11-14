"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.api.v1.router
Descripción: Router REST de la versión 1.
Provee endpoints descriptivos y metadatos estructurados sin implementar motores numéricos ficticios.
"""

from typing import Any, Dict, List, Optional
from fastapi import APIRouter, HTTPException, Query
from app.models.frontend import (
    CompareRequest,
    ComparisonPayloadFrontend,
    EarthRegion,
    FindingItem,
    ListResponse,
    MissionUseCaseFrontend,
    PlanetaryTarget,
    RegionDetailResponse,
    ScientificSourceFrontend,
)
from app.models.catalog_data import (
    CITATIONS,
    DATASETS,
    EARTH_REGIONS,
    FINDINGS,
    MISSION_USE_CASES,
    OBSERVATIONS,
    PLANETARY_TARGETS,
    SOURCES,
    build_comparison_payload,
)
from app.models.dataset import VerificationStatusEnum
from app.models.evidence import (
    ComparabilityTypeEnum,
    ScientificLimitation,
    StructuredComparison,
)
from app.models.region import (
    BoundingBox,
    CoordinateSystemTypeEnum,
    CRSDatumMetadata,
    PlanetEnum,
    PlanetaryRegion,
    TerrestrialRegion,
)

api_router = APIRouter()


@api_router.get("/info", summary="Metadatos del Proyecto e Hipótesis Científica")
def get_project_info() -> Dict[str, Any]:
    """
    Retorna la información del proyecto AnalogX, hipótesis formal y principios epistemológicos.
    """
    return {
        "project": "AnalogX — Planetary Analog Discovery Engine",
        "competition": "NASA Space Apps Challenge 2026",
        "phase": "Fase 0 — Arquitectura, Auditoría Científica y Modelado de Datos",
        "hypothesis_summary": (
            "Los depósitos de cloruro en depresiones cerradas de Terra Sirenum (Marte) exhiben "
            "firmas morfométricas relativas y de confinamiento evaporítico análogas a las observadas "
            "en el Salar de Uyuni (referencia de calibración) y campos hidrotermales de Lípez / Sol de Mañana."
        ),
        "epistemological_rules": [
            "Prohibición de comparar elevaciones absolutas entre datums incompatibles (Areoide MOLA vs Geoide EGM96).",
            "Prohibición de convertir observaciones visuales o de albedo en afirmaciones mineralógicas.",
            "Prohibición de confundir paleoprocesos marcianos con condiciones ambientales contemporáneas.",
            "La analogía no implica equivalencia ambiental total ni idoneidad para bases humanas.",
        ],
        "strict_restrictions_status": {
            "numerical_similarity_engine_active": False,
            "fictional_percentages_active": False,
            "unverified_external_downloads_active": False,
        },
    }


@api_router.get("/regions/terrestrial", response_model=List[TerrestrialRegion], summary="Regiones Terrestres Bolivianas")
def list_terrestrial_regions() -> List[TerrestrialRegion]:
    """
    Lista de regiones análogas terrestres verificadas en Bolivia (Uyuni como referencia, Sol de Mañana como novedad).
    """
    wgs84_datum = CRSDatumMetadata(
        crs_name="WGS 84 / Geographic",
        crs_code="EPSG:4326",
        datum_name="World Geodetic System 1984",
        reference_surface="Geoide EGM96",
        is_planetary=False,
        equatorial_radius_m=6378137.0,
        polar_radius_m=6356752.3142,
        flattening=0.0033528106647474805,
    )

    return [
        TerrestrialRegion(
            id="bo_salar_uyuni",
            name="Salar de Uyuni",
            country="Bolivia",
            department="Potosí / Oruro",
            province="Daniel Campos / Ladislao Cabrera",
            bounding_box=BoundingBox(
                min_lat=-20.80,
                max_lat=-19.80,
                min_lon=-68.10,
                max_lon=-67.10,
                crs_code="EPSG:4326",
            ),
            center_lat=-20.25,
            center_lon=-67.60,
            elevation_min_m=3653.0,
            elevation_max_m=3660.0,
            crs_datum=wgs84_datum,
            geological_context=(
                "Cuenca endorreica evaporítica hiperplana del Altiplano boliviano. "
                "Núcleo de halita masiva con redes poligonales de desecación de 1 a 3 m. "
                "Utilizado formalmente por NASA para calibración altimétrica."
            ),
            is_reference_site=True,
            primary_evaporite_minerals=["Halita (NaCl)", "Yeso (CaSO4·2H2O)", "Ulexita (NaCaB5O6(OH)6·5H2O)"],
            literature_references=[
                "NASA Earth Observatory (2022). Bolivian Salt Flats (Ref 15).",
                "Borsa et al. (2008). Geophysical Journal International 172(1):31-40.",
                "Risacher & Fritz (1991). Geochimica et Cosmochimica Acta 55(3):687-705.",
            ],
        ),
        TerrestrialRegion(
            id="bo_sol_de_manana",
            name="Campo Geotermal Sol de Mañana",
            country="Bolivia",
            department="Potosí",
            province="Sur Lípez",
            bounding_box=BoundingBox(
                min_lat=-22.08,
                max_lat=-22.01,
                min_lon=-67.79,
                max_lon=-67.72,
                crs_code="EPSG:4326",
            ),
            center_lat=-22.05,
            center_lon=-67.76,
            elevation_min_m=4820.0,
            elevation_max_m=5020.0,
            crs_datum=wgs84_datum,
            geological_context=(
                "Campo geotermal activo de alta entalpía a gran altitud (~4850 msnm). "
                "Fumarolas, ollas de lodo ácido hirviente, depósitos de azufre elemental y "
                "alteración por sulfatos y sílice amorfa. Análogo de vulcanismo hidrotermal del Marte temprano."
            ),
            is_reference_site=False,
            primary_evaporite_minerals=["Azufre nativo (S8)", "Alunita", "Caolinita", "Yeso", "Sílice amorfa"],
            literature_references=[
                "Cabrol et al. (2007). Journal of Geophysical Research: Biogeosciences.",
                "Squyres et al. (2008). Science 320(5879):1063-1067 (Comparación con Home Plate).",
                "Michalski et al. (2017). Nature Communications 8:15978.",
            ],
        ),
    ]


@api_router.get("/regions/planetary", response_model=List[PlanetaryRegion], summary="Regiones Planetarias de Estudio")
def list_planetary_regions() -> List[PlanetaryRegion]:
    """
    Lista de objetivos geológicos extraterrestres (Terra Sirenum en Marte).
    """
    mars_datum = CRSDatumMetadata(
        crs_name="IAU 2000 Mars / Planetocentric",
        crs_code="IAU:49900",
        datum_name="Mars 2000",
        reference_surface="Areoide MOLA (R_ecuatorial=3396.0 km)",
        is_planetary=True,
        equatorial_radius_m=3396190.0,
        polar_radius_m=3376200.0,
        flattening=0.005886,
    )

    return [
        PlanetaryRegion(
            id="mars_terra_sirenum_chloride_01",
            planet=PlanetEnum.Marte,
            target_feature_name="Depósito de cloruro de Terra Sirenum",
            regional_context="Tierras altas del sur de Marte, margen de la paleocuenca de Eridania",
            bounding_box=BoundingBox(
                min_lat=-39.30,
                max_lat=-38.30,
                min_lon=220.50,
                max_lon=221.50,
                crs_code="IAU:49900",
            ),
            center_lat=-38.80,
            center_lon=221.00,
            coordinate_system_type=CoordinateSystemTypeEnum.planetocentrico,
            crs_datum=mars_datum,
            target_type="deposito_cloruros",
            primary_references=[
                "NASA Science / JPL / ASU (2008). Chloride Salt Deposit in Southern Highlands of Mars (Ref 16).",
                "Osterloo et al. (2008). Science 319(5870):1651-1654.",
                "Osterloo et al. (2010). Journal of Geophysical Research: Planets 115(E10).",
                "Hynek et al. (2015). Geology 43(9):787-790.",
            ],
            known_instrumental_observations=[
                "HiRISE: PSP_003160_1410",
                "THEMIS: DCS B8-7-5 Mosaic",
                "MOLA: MEG128 Cuadrante Regional",
                "CRISM: FRT0000863E (Contexto regional)",
            ],
        )
    ]


@api_router.get("/comparability-matrix", response_model=List[StructuredComparison], summary="Matriz de Comparabilidad Científica")
def get_comparability_matrix() -> List[StructuredComparison]:
    """
    Retorna la evaluación estructurada de comparabilidad física entre Uyuni y Terra Sirenum.
    """
    return [
        StructuredComparison(
            id="comp_slope_uyuni_sirenum",
            terrestrial_region_id="bo_salar_uyuni",
            planetary_region_id="mars_terra_sirenum_chloride_01",
            variable_or_feature="Pendiente Topográfica Basal de Cuenca",
            comparability_type=ComparabilityTypeEnum.directa,
            resolution_compatibility="Requiere remuestreo: NASADEM (30m) vs MOLA MEG128 (463m)",
            resampling_required=True,
            physical_divergence_notes=(
                "La pendiente angular es adimensional y comparable directamente una vez homogeneizada "
                "la resolución espacial. La gravedad diferencial condiciona taludes escarpados pero no el fondo plano de sedimentación."
            ),
            scientific_limitations=[
                ScientificLimitation(
                    id="lim_gravity_01",
                    parameter_name="Gravedad superficial",
                    terrestrial_condition="9.81 m/s²",
                    planetary_condition="3.71 m/s²",
                    limitation_mechanism="Menor aceleración gravitacional en Marte permite taludes clásticos estables con pendientes ligeramente más abruptas.",
                    impact_on_analogy="No afecta fondos de cuenca horizontales hidrostáticos; afecta taludes marginales de cráteres.",
                    is_blocking_for_direct_comparison=False,
                )
            ],
            verification_status=VerificationStatusEnum.verificado_con_fuente,
            summary_conclusion="Plausibilidad alta de analogía geomorfológica para confinamiento en cuencas cerradas.",
        ),
        StructuredComparison(
            id="comp_polygons_uyuni_sirenum",
            terrestrial_region_id="bo_salar_uyuni",
            planetary_region_id="mars_terra_sirenum_chloride_01",
            variable_or_feature="Redes Poligonales de Desecación",
            comparability_type=ComparabilityTypeEnum.indirecta,
            resolution_compatibility="Compatible con imágenes submétricas: Ortofoto/S2 (1-10m) vs HiRISE PSP_003160_1410 (0.25m)",
            resampling_required=False,
            physical_divergence_notes=(
                "Los polígonos de Uyuni son dinámicos y activos anualmente bajo recarga de lluvias estacionales. "
                "Los polígonos de Terra Sirenum son fósiles de hace >3.5 Ga expuestos a meteorización eólica hiperárida."
            ),
            scientific_limitations=[
                ScientificLimitation(
                    id="lim_atmosphere_temporal_01",
                    parameter_name="Presión y ciclo hídrico temporal",
                    terrestrial_condition="~600 mbar con recarga pluvial anual activa",
                    planetary_condition="~6 mbar sin agua líquida activa contemporánea",
                    limitation_mechanism="En Marte la desecación ocurrió en el Noachiano-Hesperiano; hoy se preservan como estructuras litificadas fósiles.",
                    impact_on_analogy="La analogía modela el mecanismo formador original de contracción por pérdida de solvente, no la dinámica atmosférica actual.",
                    is_blocking_for_direct_comparison=False,
                )
            ],
            verification_status=VerificationStatusEnum.verificado_con_fuente,
            summary_conclusion="Consistencia dimensional métrica en diámetros de fracturación tensional (1 a 5 metros).",
        ),
    ]


# =========================================================================
# Endpoints de Contrato para Frontend (Fase 1 / PlannedApiContract)
# =========================================================================

@api_router.get("/regions", response_model=ListResponse[EarthRegion], summary="Listado de Regiones Terrestres para Frontend")
def get_regions(
    study_role: Optional[str] = Query(None, description="Filtro opcional por rol ('reference_calibration' o 'research_candidate')"),
    country: Optional[str] = Query(None, description="Filtro opcional por país"),
    verification_status: Optional[str] = Query(None, description="Filtro opcional por estado de verificación"),
    cursor: Optional[str] = Query(None, description="Cursor de paginación"),
) -> ListResponse[EarthRegion]:
    """
    Retorna el listado de regiones terrestres del estudio estructurado para el catálogo del frontend.
    """
    filtered = EARTH_REGIONS
    if study_role and study_role != "all":
        filtered = [r for r in filtered if r.study_role == study_role]
    if country:
        filtered = [r for r in filtered if r.country and country.lower() in r.country.lower()]
    if verification_status:
        filtered = [r for r in filtered if r.verification_status == verification_status]

    return ListResponse[EarthRegion](items=filtered, next_cursor=None)


@api_router.get("/regions/{region_id}", response_model=RegionDetailResponse, summary="Ficha Científica de Detalle de Región")
def get_region_detail(region_id: str) -> RegionDetailResponse:
    """
    Retorna la ficha de detalle de una región terrestre o planetaria con sus observaciones, datasets, fuentes y citas asociadas.
    """
    # Mapeo de alias para compatibilidad total con IDs de backend y frontend
    alias_map = {
        "bo_salar_uyuni": "salar-de-uyuni",
        "bo_sol_de_manana": "sol-de-manana",
        "bo_altiplano_sur": "altiplano-sur",
        "bo_cuevas_lipez": "cuevas-volcanicas-lipez",
        "bo_cumbre_licancabur": "cumbre-licancabur",
        "mars_terra_sirenum_chloride_01": "terra-sirenum",
        "mars_terra_sirenum": "terra-sirenum",
        "lunar_south_pole": "lunar-south-pole",
        "lunar-south-pole-shackleton": "lunar-south-pole",
    }
    normalized_id = alias_map.get(region_id, region_id)

    # Buscar en terrestres
    earth_reg = next((r for r in EARTH_REGIONS if r.id == normalized_id or r.id == region_id), None)
    target_reg = next((t for t in PLANETARY_TARGETS if t.id == normalized_id or t.id == region_id), None)

    reg = earth_reg or target_reg
    if not reg:
        raise HTTPException(status_code=404, detail=f"Región con ID '{region_id}' no encontrada en el catálogo.")

    # Filtrar entidades asociadas
    related_obs = [o for o in OBSERVATIONS if o.region_id in [normalized_id, reg.id]]
    related_datasets = [d for d in DATASETS if d.id in reg.dataset_ids]
    related_sources = [s for s in SOURCES if any(d.source_id == s.id for d in related_datasets)]
    related_citations = [c for c in CITATIONS if c.id in reg.citation_ids]
    related_use_cases = [
        u for u in MISSION_USE_CASES
        if u.earth_region_id in [normalized_id, reg.id] or u.planetary_target_id in [normalized_id, reg.id]
    ]

    return RegionDetailResponse(
        region=reg,
        observations=related_obs,
        datasets=related_datasets,
        sources=related_sources,
        citations=related_citations,
        mission_use_cases=related_use_cases,
    )


@api_router.get("/missions/use-cases", response_model=ListResponse[MissionUseCaseFrontend], summary="Casos de Uso Operacionales para Misiones Espaciales")
def list_mission_use_cases(
    category: Optional[str] = Query(None, description="Filtro opcional por categoría de misión"),
    earth_region_id: Optional[str] = Query(None, description="Filtro opcional por región análoga terrestre"),
    planetary_target_id: Optional[str] = Query(None, description="Filtro opcional por objetivo planetario"),
) -> ListResponse[MissionUseCaseFrontend]:
    """
    Retorna los casos de uso para misiones espaciales reales (NASA Artemis, rovers, ISRU, calibración instrumental).
    """
    cases = MISSION_USE_CASES
    if category:
        cases = [c for c in cases if c.category == category]
    if earth_region_id:
        cases = [c for c in cases if c.earth_region_id == earth_region_id]
    if planetary_target_id:
        cases = [c for c in cases if c.planetary_target_id == planetary_target_id]
    return ListResponse[MissionUseCaseFrontend](items=cases, next_cursor=None)


@api_router.get("/targets", response_model=ListResponse[PlanetaryTarget], summary="Objetivos Planetarios Extraterrestres")
def get_targets(
    body: Optional[str] = Query(None, description="Filtro opcional por cuerpo ('Mars' o 'Moon')"),
    cursor: Optional[str] = Query(None, description="Cursor de paginación"),
) -> ListResponse[PlanetaryTarget]:
    """
    Retorna el listado de objetivos planetarios de estudio (Terra Sirenum en Marte, Objetivo Lunar).
    """
    targets = PLANETARY_TARGETS
    if body:
        targets = [t for t in targets if t.body.lower() == body.lower()]
    return ListResponse[PlanetaryTarget](items=targets, next_cursor=None)


@api_router.post("/compare", response_model=ComparisonPayloadFrontend, summary="Comparación Estructurada Tierra vs Marte/Luna")
def compare_environments(request: CompareRequest) -> ComparisonPayloadFrontend:
    """
    Evalúa la compatibilidad variable a variable entre un análogo terrestre y un objetivo planetario.
    Incluye aviso epistemológico obligatorio de habitabilidad y limitaciones físicas explícitas.
    """
    return build_comparison_payload(request.earth_region_id, request.planetary_target_id)


@api_router.get("/sources", response_model=ListResponse[ScientificSourceFrontend], summary="Fuentes Científicas Oficiales")
def list_sources(
    cursor: Optional[str] = Query(None, description="Cursor de paginación"),
) -> ListResponse[ScientificSourceFrontend]:
    """
    Retorna el listado de organismos científicos oficiales y repositorios de datos indexados.
    """
    return ListResponse[ScientificSourceFrontend](items=SOURCES, next_cursor=None)


@api_router.get("/findings", response_model=List[FindingItem], summary="Bitácora de Hallazgos Científicos Validados")
def list_findings() -> List[FindingItem]:
    """
    Retorna los hallazgos científicos consolidados a partir de las evidencias y comparaciones auditadas.
    """
    return FINDINGS


