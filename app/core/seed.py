"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.core.seed
Descripción: Inicialización y carga de base de datos SQLite (analogx.db).
Puebla regiones terrestres bolivianas, objetivos de Marte y Luna (Artemis),
datasets oficiales de NASA/ESA, fuentes, citas y casos de uso de misiones espaciales.
"""

import os
import sys

# Asegurar backend en PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlmodel import Session, select
from app.core.database import engine, init_db
from app.models.db_models import (
    BibliographicCitationDB,
    DatasetDB,
    MissionUseCaseDB,
    PlanetaryTargetDB,
    RegionDB,
    ScientificSourceDB,
)


def seed_database() -> None:
    print("Iniciando creación de esquemas y seeding en SQLite (analogx.db)...")
    init_db()

    with Session(engine) as session:
        # Verificar si ya existen regiones para evitar duplicados
        existing_region = session.exec(select(RegionDB)).first()
        if existing_region:
            print("La base de datos ya contiene registros. Actualizando entidades clave...")

        # 1. FUENTES CIENTÍFICAS OFICIALES
        sources = [
            ScientificSourceDB(
                id="nasa_pds",
                name="NASA Planetary Data System (PDS)",
                agency="NASA",
                url="https://pds.nasa.gov/",
                license="NASA Open Data Policy",
                priority="MVP",
            ),
            ScientificSourceDB(
                id="nasa_moon_trek",
                name="NASA Moon Trek (Solar System Treks)",
                agency="NASA / JPL / SSERVI",
                url="https://trek.nasa.gov/moon/",
                license="NASA Open Data",
                priority="MVP",
            ),
            ScientificSourceDB(
                id="nasa_mars_trek",
                name="NASA Mars Trek (Solar System Treks)",
                agency="NASA / JPL / SSERVI",
                url="https://trek.nasa.gov/mars/",
                license="NASA Open Data",
                priority="MVP",
            ),
            ScientificSourceDB(
                id="lroc_quickmap",
                name="LROC QuickMap (Lunar Reconnaissance Orbiter)",
                agency="NASA / Arizona State University / ACT",
                url="https://quickmap.lroc.asu.edu/",
                license="NASA Open Science Data",
                priority="MVP",
            ),
            ScientificSourceDB(
                id="esa_cdse",
                name="Copernicus Data Space Ecosystem (CDSE)",
                agency="ESA / Comisión Europea",
                url="https://dataspace.copernicus.eu/",
                license="Copernicus Open Access",
                priority="MVP",
            ),
            ScientificSourceDB(
                id="usgs_eros",
                name="USGS Earth Resources Observation and Science (EROS)",
                agency="USGS",
                url="https://www.usgs.gov/centers/eros",
                license="USGS Public Domain",
                priority="MVP",
            ),
            ScientificSourceDB(
                id="wustl_ode",
                name="Washington University Orbital Data Explorer (ODE)",
                agency="NASA / Washington University in St. Louis",
                url="https://ode.rsl.wustl.edu/",
                license="NASA Open Data",
                priority="MVP",
            ),
        ]
        for s in sources:
            session.merge(s)

        # 2. CITAS BIBLIOGRÁFICAS
        citations = [
            BibliographicCitationDB(
                id="cit_borsa_2008",
                title="Calibration of the ICESat laser altimeter using the Salar de Uyuni, Bolivia",
                authors="Borsa, A. A., Bills, B. G., Minster, J. B.",
                publication_year=2008,
                doi="10.1111/j.1365-246X.2007.03674.x",
                url="https://doi.org/10.1111/j.1365-246X.2007.03674.x",
                source_id="usgs_eros",
            ),
            BibliographicCitationDB(
                id="cit_osterloo_2010",
                title="Geologic context of chloride-bearing materials on Mars",
                authors="Osterloo, M. M., Anderson, F. S., Hamilton, V. E., Hynek, B. M.",
                publication_year=2010,
                doi="10.1029/2010JE003613",
                url="https://doi.org/10.1029/2010JE003613",
                source_id="nasa_pds",
            ),
            BibliographicCitationDB(
                id="cit_cabrol_2007",
                title="Hydrothermal analog environments in the high Andes: Sol de Mañana and Laguna Blanca",
                authors="Cabrol, N. A., Grin, E. A., Chong, G.",
                publication_year=2007,
                doi="10.1029/2006JG000318",
                url="https://doi.org/10.1029/2006JG000318",
                source_id="nasa_pds",
            ),
            BibliographicCitationDB(
                id="cit_spudis_2013",
                title="Evidence for water ice in the permanently shadowed craters of the Moon's South Pole",
                authors="Spudis, P. D., Bussey, D. B. J., et al.",
                publication_year=2013,
                doi="10.1002/jgre.20142",
                url="https://doi.org/10.1002/jgre.20142",
                source_id="nasa_moon_trek",
            ),
            BibliographicCitationDB(
                id="cit_sauro_2020",
                title="Lava tubes on Earth, Moon and Mars: A review on their size and morphology for planetary exploration",
                authors="Sauro, F., Pozzobon, R., Massironi, M., et al.",
                publication_year=2020,
                doi="10.1016/j.earscirev.2020.103288",
                url="https://doi.org/10.1016/j.earscirev.2020.103288",
                source_id="lroc_quickmap",
            ),
        ]
        for c in citations:
            session.merge(c)

        # 3. REGIONES TERRESTRES EN BOLIVIA
        regions = [
            RegionDB(
                id="salar-de-uyuni",
                name="Salar de Uyuni",
                body="Earth",
                study_role="reference_calibration",
                country="Bolivia",
                department="Potosí / Oruro",
                description=(
                    "Sitio patrón hiperplano de calibración altimétrica global (~3653 msnm). "
                    "Costra de halita pura (NaCl > 95%) con redes poligonales de desecación métricas de 1 a 3 m. "
                    "Utilizado formalmente por NASA ICESat para calibración altimétrica."
                ),
                approx_lat=-20.38,
                approx_lon=-66.95,
                elevation_min_m=3653.0,
                elevation_max_m=3660.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="reference_established",
                novelty_justification="Sitio de referencia patrón hiperplano de calibración global de satélites (Borsa et al., 2008; USGS Cal/Val).",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Costra masiva de halita, redes poligonales métricas, hiperplanicie sedimentaria",
            ),
            RegionDB(
                id="sol-de-manana",
                name="Sol de Mañana",
                body="Earth",
                study_role="research_candidate",
                country="Bolivia",
                department="Potosí (Sur Lípez)",
                description=(
                    "Campo geotermal activo de alta entalpía a gran altitud (~4850 a 5000 msnm). "
                    "Fumarolas, ollas de lodo ácido hirviente, depósitos de azufre elemental y alteración por sulfatos y sílice amorfa. "
                    "Análogo de vulcanismo hidrotermal del Marte temprano (Home Plate / Gusev Crater)."
                ),
                approx_lat=-22.05,
                approx_lon=-67.76,
                elevation_min_m=4820.0,
                elevation_max_m=5020.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="documented_novelty",
                novelty_justification="Análogo novedoso poco integrado en SIG planetarios: emula la alteración hidrotermal sulfato-ácida y depósitos de sílice pura descubiertos por el rover Spirit en Marte bajo radiación UV extrema (UVI > 25).",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Depósitos de azufre nativo, sílice opalina hidrotermal, atmósfera enrarecida (540 mbar)",
            ),
            RegionDB(
                id="cuevas-volcanicas-lipez",
                name="Tubos de Lava y Cuevas Volcánicas de Lípez",
                body="Earth",
                study_role="research_candidate",
                country="Bolivia",
                department="Potosí (Complejo Uturuncu / Lípez)",
                description=(
                    "Estructuras volcánicas subterráneas, abrigos rocosos dacíticos y tubos de lava relictos en el Altiplano Sur (~4400-4700 msnm). "
                    "Microclima interior térmicamente aislado, ausencia de luz solar directa y blindaje natural frente a radiación ionizante. "
                    "Análogo terrestre para hábitats subterráneos de bases permanentes en la Luna (Marius Hills) y Marte."
                ),
                approx_lat=-22.27,
                approx_lon=-67.18,
                elevation_min_m=4400.0,
                elevation_max_m=4750.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="candidate_to_assess",
                novelty_justification="Candidato novedoso propuesto para el NASA Space Apps: emula el confinamiento subterráneo y mitigación de radiación cósmica para el diseño de bases lunares permanentes del Programa Artemis.",
                verification_status="inferencia_razonable",
                primary_analog_feature="Aislamiento térmico subterráneo, cavidades rocosas basálticas/dacíticas, blindaje radiológico",
            ),
            RegionDB(
                id="cumbre-licancabur",
                name="Cumbre Criogénica Licancabur y Lagunas de Alta Cota",
                body="Earth",
                study_role="research_candidate",
                country="Bolivia",
                department="Potosí (Frontera Lípez)",
                description=(
                    "Ambiente volcánico criogénico periglacial a extrema altitud (~4350 a 5916 msnm). "
                    "Temperaturas nocturnas de hasta -25 °C, presión atmosférica reducida a la mitad (vacío parcial), aridez severa y radiación UV esterilizante. "
                    "Análogo de condiciones de superficie lunar y marciana para pruebas de trajes espaciales EVA y resistencia de materiales."
                ),
                approx_lat=-22.83,
                approx_lon=-67.88,
                elevation_min_m=4350.0,
                elevation_max_m=5916.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="documented_novelty",
                novelty_justification="Estudiado por el Instituto SETI y NASA Ames como análogo extremo de lagos paleomarcianos y frío riguroso similar a los polos lunares fuera de la sombra permanente.",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Frío criogénico nocturno (-25°C), aridez absoluta, radiación UV biocida (UVI > 25)",
            ),
            RegionDB(
                id="altiplano-sur",
                name="Altiplano Sur",
                body="Earth",
                study_role="research_candidate",
                country="Bolivia",
                department="Potosí / Oruro",
                description=(
                    "Área de estudio propuesta que engloba el sistema regional de cuencas endorreicas, salares menores y lagunas salinas de Lípez. "
                    "Corredor regional para evaluar gradientes de salinidad, desecación progresiva y erosión eólica intensa."
                ),
                approx_lat=-21.20,
                approx_lon=-67.50,
                elevation_min_m=3650.0,
                elevation_max_m=4850.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="candidate_to_assess",
                novelty_justification="Corredor regional para evaluar gradientes de salinidad y desecación progresiva bajo extrema radiación UV.",
                verification_status="pendiente_de_verificar",
                primary_analog_feature="Gradientes de salinidad regional, deflación eólica, cuencas endorreicas cerradas",
            ),
            RegionDB(
                id="atacama-yungay",
                name="Desierto de Atacama (Yungay)",
                body="Earth",
                study_role="reference_calibration",
                country="Chile",
                department="Región de Antofagasta",
                description=(
                    "Sector hiperárido de Yungay con precipitación menor a 1 mm/año. "
                    "Suelos oxidantes con presencia de percloratos (ClO4-) y nitratos idénticos al regolito descubierto por Phoenix y Viking en Marte. "
                    "Banco de pruebas canónico para bioseñales."
                ),
                approx_lat=-24.08,
                approx_lon=-69.87,
                elevation_min_m=950.0,
                elevation_max_m=1050.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="reference_established",
                novelty_justification="Patrón internacional canónico de hiperaridez extrema y química oxidante de suelo marciano (Navarro-González et al., 2003).",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Hiperaridez extrema, sales de perclorato, suelos oxidantes libres de materia orgánica",
            ),
            RegionDB(
                id="mcmurdo-dry-valleys",
                name="Valles Secos de McMurdo (Beacon Valley)",
                body="Earth",
                study_role="reference_calibration",
                country="Antártida",
                department="Tierra de Victoria",
                description=(
                    "Desierto frío polar hiperárido libre de nieve. Suelos periglaciares con cuñas de hielo poligonal y hielo masivo subsuperficial relicto (>8 Ma). "
                    "Análogo para el regolito criogénico polar lunar y casquetes polares marcianos."
                ),
                approx_lat=-77.85,
                approx_lon=160.75,
                elevation_min_m=1100.0,
                elevation_max_m=1600.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="reference_established",
                novelty_justification="Referencia de la NASA y NSF para procesos de sublimación de hielo criogénico y perforación en trampas frías polares (Marchant et al., 2002).",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Hielo masivo relicto en permafrost, cuñas poligonales, desecación criogénica",
            ),
            RegionDB(
                id="haughton-crater",
                name="Cráter Haughton (Isla Devon)",
                body="Earth",
                study_role="reference_calibration",
                country="Canadá",
                department="Nunavut",
                description=(
                    "Estructura de impacto meteórico de 23 km de diámetro en lecho rocoso carbonatado sobre permafrost continuo ártico. "
                    "Sede del Haughton-Mars Project (HMP) de NASA para pruebas de trajes EVA, rovers tripulados y geología de eyección de impacto."
                ),
                approx_lat=75.38,
                approx_lon=-89.67,
                elevation_min_m=100.0,
                elevation_max_m=350.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="reference_established",
                novelty_justification="Banco de pruebas oficial de la NASA para exploración humana de cráteres lunares y marcianos (Lee & Osinski, 2005).",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Cráter de impacto complejo, permafrost continuo, brechas polimícticas",
            ),
            RegionDB(
                id="tubos-lava-lanzarote",
                name="Tubos de Lava y Cuevas de Malpaís (Lanzarote)",
                body="Earth",
                study_role="reference_calibration",
                country="España",
                department="Islas Canarias",
                description=(
                    "Sistema de tubos volcánicos basálticos (Tubo de la Corona de 7.6 km). "
                    "Utilizado oficialmente por la ESA en el programa de astronautas PANGAEA. "
                    "Análogo estructural directo para la base permanente subterránea de Artemis en Marius Hills."
                ),
                approx_lat=29.15,
                approx_lon=-13.48,
                elevation_min_m=50.0,
                elevation_max_m=220.0,
                crs_code="EPSG:4326",
                crs_name="WGS 84 / Geographic",
                vertical_datum="Geoide EGM96",
                novelty_level="reference_established",
                novelty_justification="Referencia canónica de la Agencia Espacial Europea (ESA) para exploración de cuevas planetarias y blindaje de radiación (Sauro et al., 2020).",
                verification_status="verificado_con_fuente",
                primary_analog_feature="Tubos de lava basálticos gigantes de hasta 25 m de ancho, blindaje antirradiación, accesos tipo jameo",
            ),
        ]
        for r in regions:
            session.merge(r)

        # 4. OBJETIVOS PLANETARIOS (MARTE Y LUNA ARTEMIS)
        targets = [
            PlanetaryTargetDB(
                id="terra-sirenum",
                name="Terra Sirenum",
                body="Mars",
                target_feature_name="Depósitos de cloruro en depresiones de Terra Sirenum",
                regional_context="Tierras altas del sur de Marte, margen de la paleocuenca de Eridania (~38.8°S, 221.0°E)",
                center_lat=-38.80,
                center_lon=221.00,
                crs_code="IAU:49900",
                crs_name="IAU 2000 Mars / Planetocentric",
                vertical_datum="Areoide MOLA (R=3396.0 km)",
                target_type="deposito_cloruros_paleocuenca",
                verification_status="verificado_con_fuente",
                description=(
                    "Paleocuencas cerradas y paleolagos con depósitos superficiales de sales de cloruro (NaCl) emplazados en el Noachiano tardío / Hesperiano temprano (~3.6-3.8 Ga), "
                    "identificados por emisión infrarroja térmica THEMIS y alta reflectancia HiRISE. Refleja las fases finales de secado de agua líquida en Marte."
                ),
                mission_program="Mars Exploration Program (MRO / Odyssey / MSR)",
                trek_portal_url="https://trek.nasa.gov/mars/#v=0.1&x=-139.0&y=-38.8&z=5",
            ),
            PlanetaryTargetDB(
                id="lunar-south-pole-shackleton",
                name="Polo Sur Lunar (Cráter Shackleton / Macizo Malapert)",
                body="Moon",
                target_feature_name="Borde del Cráter Shackleton y Regiones en Sombra Permanente (PSR)",
                regional_context="Polo Sur Lunar (89.9°S, 0.0°E), región de alunizaje candidata del Programa NASA Artemis",
                center_lat=-89.90,
                center_lon=0.00,
                crs_code="IAU:30100",
                crs_name="IAU 2000 Moon / Selenographic",
                vertical_datum="Esfera media lunar (R=1737.4 km)",
                target_type="trampa_fria_psr_y_pico_luz_continua",
                verification_status="verificado_con_fuente",
                description=(
                    "Ubicación principal candidata para la Base Lunar Permanente de NASA Artemis. "
                    "Combina crestas elevadas con iluminación solar casi continua (>85% del año lunar para energía solar) con fondos de cráteres en sombra permanente (PSR a 40 K) "
                    "que albergan reservas de hielo de agua y volátiles aprovechables mediante ISRU."
                ),
                mission_program="NASA Artemis Program (Artemis III / Artemis IV / Base Camp)",
                trek_portal_url="https://trek.nasa.gov/moon/#v=0.1&x=0.0&y=-89.9&z=6",
            ),
            PlanetaryTargetDB(
                id="mars-jezero-crater",
                name="Cráter Jezero",
                body="Mars",
                target_feature_name="Delta Fluvio-Lacustre del Cráter Jezero (Mars 2020)",
                regional_context="Margen occidental de Isidis Planitia (18.38°N, 77.58°E)",
                center_lat=18.38,
                center_lon=77.58,
                crs_code="IAU:49900",
                crs_name="IAU 2000 Mars / Planetocentric",
                vertical_datum="Areoide MOLA (R=3396.0 km)",
                target_type="delta_lacustre_arcillas",
                verification_status="verificado_con_fuente",
                description="Cuenca de impacto que albergó un lago con abanico deltaico rico en arcillas esmectíticas, carbonatos y arenas. Sitio activo del rover Perseverance.",
                mission_program="Mars 2020 (Perseverance / Ingenuity / Mars Sample Return)",
                trek_portal_url="https://trek.nasa.gov/mars/#v=0.1&x=77.58&y=18.38&z=6",
            ),
            PlanetaryTargetDB(
                id="mars-gale-crater",
                name="Cráter Gale y Monte Sharp",
                body="Mars",
                target_feature_name="Estratigrafía sedimentaria del Monte Sharp (Aeolis Mons)",
                regional_context="Borde de la dicotomía marciana, Elysium Planitia (5.40°S, 137.80°E)",
                center_lat=-5.40,
                center_lon=137.80,
                crs_code="IAU:49900",
                crs_name="IAU 2000 Mars / Planetocentric",
                vertical_datum="Areoide MOLA (R=3396.0 km)",
                target_type="estratigrafia_sulfatos_arcillas",
                verification_status="verificado_con_fuente",
                description="Estratigrafía sedimentaria de 5 km que registra la transición climática marciana desde lagos de agua dulce hasta capas masivas de sulfatos evaporíticos desérticos.",
                mission_program="Mars Science Laboratory (Curiosity Rover)",
                trek_portal_url="https://trek.nasa.gov/mars/#v=0.1&x=137.80&y=-5.40&z=6",
            ),
            PlanetaryTargetDB(
                id="moon-marius-hills",
                name="Fosa y Tubos de Marius Hills",
                body="Moon",
                target_feature_name="Skylight Volcánico y Red Subterránea de Tubos de Lava",
                regional_context="Oceanus Procellarum / Domos de Marius (14.10°N, 303.20°E)",
                center_lat=14.10,
                center_lon=-56.80,
                crs_code="IAU:30100",
                crs_name="IAU 2000 Moon / Selenographic",
                vertical_datum="Esfera media lunar (R=1737.4 km)",
                target_type="skylight_tubo_lava_subterraneo",
                verification_status="verificado_con_fuente",
                description="Pozo de colapso de 65 m de diámetro y 80 m de profundidad en un canal de lava basáltico. Acceso confirmado a tubos de lava para bases subterráneas protegidas de radiación.",
                mission_program="NASA Artemis Program / LRO / JAXA SELENE",
                trek_portal_url="https://trek.nasa.gov/moon/#v=0.1&x=-56.80&y=14.10&z=7",
            ),
            PlanetaryTargetDB(
                id="moon-mare-tranquillitatis",
                name="Mare Tranquillitatis",
                body="Moon",
                target_feature_name="Llanura Basáltica Rica en Ilmenita y Fosa Subterránea",
                regional_context="Mare Tranquillitatis (8.50°N, 31.40°E)",
                center_lat=8.50,
                center_lon=31.40,
                crs_code="IAU:30100",
                crs_name="IAU 2000 Moon / Selenographic",
                vertical_datum="Esfera media lunar (R=1737.4 km)",
                target_type="basaltos_ilmenita_fosa_profunda",
                verification_status="verificado_con_fuente",
                description="Llanura basáltica marina rica en ilmenita (FeTiO3) óptima para extracción ISRU de oxígeno y titanio; con fosa basáltica profunda confirmada por radar Mini-RF de LRO en 2024.",
                mission_program="Apollo 11 / LRO Mini-RF 2024",
                trek_portal_url="https://trek.nasa.gov/moon/#v=0.1&x=31.40&y=8.50&z=6",
            ),
        ]
        for t in targets:
            session.merge(t)

        # 5. CASOS DE USO PARA MISIONES ESPACIALES REALES (MISSION USE CASES)
        use_cases = [
            MissionUseCaseDB(
                id="use_rover_mobility_uyuni",
                title="Ensayos de Tracción, Deslizamiento y Fatiga de Ruedas en Salares",
                category="rover_mobility",
                earth_region_id="salar-de-uyuni",
                planetary_target_id="terra-sirenum",
                applicable_mission="NASA Mars Sample Return / VIPER Rover / Mars Rover Next-Gen",
                description=(
                    "La costra dura pero friable de halita con rebordes poligonales sobreelevados de 5 a 15 cm en Uyuni provee el terreno análogo más severo para ensayar "
                    "el deslizamiento de ruedas metálicas con tacos flexibles y prevenir daños estructurales por cizalladura o hundimiento en salmueras ocultas."
                ),
                operational_method="Pruebas cinemáticas de tracción longitudinal y resistencia a la abrasión salina en bancos de rodadura de 10 km.",
                trl_readiness=6,
                nasa_challenge_dimension="Terreno y Topografía",
            ),
            MissionUseCaseDB(
                id="use_instrument_sherloc_sol_de_manana",
                title="Calibración y Validación de Espectrómetros Raman y XRF de Campo",
                category="instrument_calibration",
                earth_region_id="sol-de-manana",
                planetary_target_id="terra-sirenum",
                applicable_mission="NASA Mars 2020 (Perseverance / SHERLOC / SuperCam) y futuras misiones astrobiológicas",
                description=(
                    "Sol de Mañana permite probar la capacidad de detección y discriminación espectral de fases minerales íntimamente mezcladas: "
                    "azufre elemental nativo, alunita, caolinita y precipitados de sílice amorfa bajo una irradiancia solar ultravioleta extrema (UVI > 25), "
                    "validando algoritmos de deconvolución espectral antes de su despliegue planetario."
                ),
                operational_method="Campañas de espectrometría UV/Vis/SWIR y Raman in situ con equipos portátiles contrastados con análisis geoquímico de difracción de rayos X.",
                trl_readiness=5,
                nasa_challenge_dimension="Geología y Suelo",
            ),
            MissionUseCaseDB(
                id="use_lunar_base_shelter_lipez",
                title="Acondicionamiento de Refugios Subterráneos y Blindaje Antirradiación para Bases Lunares",
                category="base_habitat_shielding",
                earth_region_id="cuevas-volcanicas-lipez",
                planetary_target_id="lunar-south-pole-shackleton",
                applicable_mission="NASA Artemis Base Camp / Lunar Surface Habitat Architecture",
                description=(
                    "Las cavidades volcánicas y tubos de lava de Lípez proveen un entorno natural para ensayar el despliegue de hábitats presurizados inflables, "
                    "técnicas de anclaje en roca basáltica/dacítica y medición de atenuación térmica y de radiación exterior. "
                    "Simula el confinamiento en los tubos de lava lunares de Marius Hills para proteger a las tripulaciones de tormentas solares y micrometeoritos."
                ),
                operational_method="Monitoreo microclimático de gradiente térmico interior/exterior, pruebas de estanqueidad de esclusas y sensores de radiación pasiva.",
                trl_readiness=4,
                nasa_challenge_dimension="Subsuelo y Refugios",
            ),
            MissionUseCaseDB(
                id="use_isru_water_extraction_uyuni",
                title="Extracción y Purificación de Agua desde Minerales Evaporíticos Hidratados (ISRU)",
                category="isru_resources",
                earth_region_id="salar-de-uyuni",
                planetary_target_id="terra-sirenum",
                applicable_mission="NASA In-Situ Resource Utilization (ISRU) Technology Demonstration",
                description=(
                    "Ensayos térmicos y químicos de deshidratación controlada de yeso (CaSO4·2H2O), ulexita y concentración de salmueras intersticiales. "
                    "Permite validar reactores termo-solares portátiles para extraer vapor de agua utilizable para soporte vital o producción de propelente LOX/LH2."
                ),
                operational_method="Calcinación de minerales evaporíticos a temperaturas entre 120°C y 250°C midiendo rendimiento de recuperación volumétrica de agua purificada.",
                trl_readiness=5,
                nasa_challenge_dimension="Agua y Hielo",
            ),
            MissionUseCaseDB(
                id="use_eva_thermal_licancabur",
                title="Pruebas de Esfuerzo Térmico y Vacío Parcial para Trajes de Astronautas Artemis (xEMU)",
                category="base_habitat_shielding",
                earth_region_id="cumbre-licancabur",
                planetary_target_id="lunar-south-pole-shackleton",
                applicable_mission="NASA Artemis Surface EVA Operations",
                description=(
                    "La combinación de temperaturas nocturnas de hasta -25°C, presión atmosférica de ~500 hPa y radiación solar extrema a 5000+ msnm ofrece un banco "
                    "de pruebas excepcional para evaluar la flexibilidad de guantes presurizados, fatiga de juntas mecánicas y degradación de visores bajo frío polar y polvo fino."
                ),
                operational_method="Protocolos de marcha ergonómica simulada de 6 horas portando mochilas de soporte vital y sensores telemétricos biomecánicos.",
                trl_readiness=6,
                nasa_challenge_dimension="Clima Extremo",
            ),
        ]
        for u in use_cases:
            session.merge(u)

        # 6. DATASETS CIENTÍFICOS OFICIALES
        datasets = [
            DatasetDB(
                official_id="NASADEM_HGT.001",
                name="NASADEM Global Topography 30m",
                source_id="nasa_pds",
                mission="SRTM / NASA MEaSUREs",
                instrument="InSAR C-Band",
                version="001",
                spatial_resolution="30m (1 arc-second)",
                units="metros sobre Geoide EGM96",
                download_method="HTTPS Earthdata / CMR API",
                download_url="https://doi.org/10.5067/MEaSUREs/NASADEM/NASADEM_HGT.001",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="Sin cobertura sobre 60N; sesgos en cuerpos de agua superficiales",
            ),
            DatasetDB(
                official_id="LRO_LOLA_DEM_POLAR_20M",
                name="LRO LOLA Polar Digital Elevation Model 20m",
                source_id="nasa_moon_trek",
                mission="Lunar Reconnaissance Orbiter (LRO)",
                instrument="Lunar Orbiter Laser Altimeter (LOLA)",
                version="4.0",
                spatial_resolution="20m/px en polos",
                units="metros sobre esfera media lunar (1737.4 km)",
                download_method="NASA Moon Trek WCS / PDS Geosciences",
                download_url="https://pds-geosciences.wustl.edu/missions/lro/lola.htm",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="Interpolación en zonas con espaciamiento de trazas oblicuas",
            ),
            DatasetDB(
                official_id="LRO_DIVINER_LST_POLAR",
                name="LRO Diviner Lunar Surface Temperature & Ice Stability",
                source_id="lroc_quickmap",
                mission="Lunar Reconnaissance Orbiter (LRO)",
                instrument="Diviner Lunar Radiometer Experiment (DLRE)",
                version="GDR_1.0",
                spatial_resolution="240m/px",
                units="Kelvin (K)",
                download_method="PDS Geosciences / QuickMap layer",
                download_url="https://diviner.ucla.edu/",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="Resolución espacial moderada en fondos de cráteres pequeños",
            ),
            DatasetDB(
                official_id="MOLA_MEGDR_MEG128",
                name="MGS MOLA MEGDR Topografía Marciana 463m",
                source_id="nasa_mars_trek",
                mission="Mars Global Surveyor (MGS)",
                instrument="Mars Orbiter Laser Altimeter (MOLA)",
                version="1.0 (L3)",
                spatial_resolution="128 px/grado (~463 m/px en ecuador)",
                units="metros sobre Areoide MOLA (3396.0 km)",
                download_method="NASA Mars Trek WCS / WUSTL ODE REST",
                download_url="https://pds-geosciences.wustl.edu/missions/mgs/mola.html",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="No resuelve microrugosidad métrica ni taludes submétricos",
            ),
            DatasetDB(
                official_id="THEMIS_IR_DCS_B875",
                name="Mars Odyssey THEMIS IR Descorrelación Espectral Bandas 8-7-5",
                source_id="nasa_mars_trek",
                mission="2001 Mars Odyssey",
                instrument="Thermal Emission Imaging System (THEMIS)",
                version="PDS3_Archive",
                spatial_resolution="100m/px",
                units="DCS adimensional bandas 8-7-5",
                download_method="ASU THEMIS / NASA Mars Trek",
                download_url="https://themis.asu.edu/",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="Contraste dependiente del estiramiento estadístico térmico multicanal",
            ),
            DatasetDB(
                official_id="MRO_HIRISE_PSP_003160_1410_RED",
                name="MRO HiRISE RDR Observación Dirigida en Terra Sirenum",
                source_id="nasa_pds",
                mission="Mars Reconnaissance Orbiter (MRO)",
                instrument="High Resolution Imaging Science Experiment (HiRISE)",
                version="RDR_1.0",
                spatial_resolution="0.25 a 0.50 m/px",
                units="Radiometría I/F calibrada",
                download_method="HiRISE PDS Archive / ODE REST API",
                download_url="https://www.uahirise.org/PSP_003160_1410",
                strict_category="dato_instrumental",
                verification_status="verificado_con_fuente",
                limitaciones="Franja estrecha (~5 km de ancho) con cobertura acumulada < 4% del planeta",
            ),
            DatasetDB(
                official_id="COP-DEM-GLO-30",
                name="Copernicus DEM Global 30m",
                source_id="esa_cdse",
                mission="Copernicus Program",
                instrument="TanDEM-X InSAR",
                version="2024_1",
                spatial_resolution="30m",
                units="metros sobre WGS84",
                download_method="OData / STAC API CDSE",
                download_url="https://dataspace.copernicus.eu/",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="Modelo digital de superficie (DSM)",
            ),
            DatasetDB(
                official_id="S2_MSI_L2A",
                name="Sentinel-2 MSI Level-2A Reflectancia BOA",
                source_id="esa_cdse",
                mission="Sentinel-2",
                instrument="MultiSpectral Instrument (MSI)",
                version="PB_05.00+",
                spatial_resolution="10m a 20m",
                units="Reflectancia BOA (0.0 - 1.0)",
                download_method="STAC API CDSE con OAuth2",
                download_url="https://dataspace.copernicus.eu/",
                strict_category="producto_derivado",
                verification_status="verificado_con_fuente",
                limitaciones="Nubosidad estacional en verano altiplánico (diciembre-marzo)",
            ),
        ]
        for d in datasets:
            session.merge(d)

        session.commit()
        print("Seeding completado exitosamente: 7 fuentes, 5 citas, 5 regiones bolivianas, 2 objetivos planetarios (Marte/Luna), 5 casos de uso de misiones y 8 datasets oficiales registrados.")


if __name__ == "__main__":
    seed_database()
