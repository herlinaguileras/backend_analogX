# ARQUITECTURA DE DATOS CIENTÍFICOS Y SISTEMA DE REFERENCIA ESPACIAL
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `docs/scientific-data-architecture.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Estatus:** Arquitectura de referencia  

---

## 1. VISIÓN GENERAL DE LA ARQUITECTURA DEL BACKEND

AnalogX Backend adopta una **arquitectura en capas modular y orientada al dominio científico (Clean Scientific Architecture)**, diseñada para garantizar:
1. **Separación estricta entre Hechos Instrumentales e Inferencias:**  
   Los datos crudos de sensores (ej. reflectancia I/F de HiRISE, altura MOLA) se aíslan de las interpretaciones bibliográficas y de los productos derivados.
2. **Invariancia de Datum y Sistemas de Coordenadas:**  
   Ninguna operación matemática entre datos terrestres y marcianos se realiza en sistemas de coordenadas absolutos.
3. **Trazabilidad Completa (Evidence Ledger):**  
   Cada medición expuesta por la API contiene metadatos de autoría, URL de origen, versión de producto, resolución, incertidumbre y estado de verificación.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           API GATEWAY / FASTAPI                         │
│   /api/v1/regions  |  /api/v1/datasets  |  /api/v1/observations  | ...   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────▼────────────────────────────────────┐
│                  CAPA DE DOMINIO Y MODELOS (PYDANTIC)                   │
│   DatasetMetadata  |  TerrestrialRegion  |  PlanetaryRegion            │
│   ObservationMeasurement  |  StructuredComparison  |  Evidence          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────▼────────────────────────────────────┐
│           CAPA DE NORMALIZACIÓN Y HOMOGENEIZACIÓN CIENTÍFICA            │
│   - Relieve Relativo (z - z_min)      - Remuestreo Espacial             │
│   - Desacoplamiento Dimensional       - Clasificador de Comparabilidad  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────▼────────────────────────────────────┐
│                    LEDGER DE EVIDENCIAS CIENTÍFICAS                     │
│   - Repositorio Inmutable de Metadatos y Mediciones Fácticas             │
│   - Registro de Estados: Verificado | Inferencia | Hipótesis | Pendiente │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
┌────────────────────────────────────▼────────────────────────────────────┐
│                 ADAPTADORES DE INGESTA DE FUENTES ABIERTAS              │
│   NASA CMR / AppEEARS  |  ESA CDSE STAC  |  NASA PDS / ODE  | CSA SAR   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. GESTIÓN DE SISTEMAS DE COORDENADAS (CRS) Y DATUMS PLANETARIOS

Uno de los principales errores en sistemas SIG multiplataforma consiste en asumir que las proyecciones terrestres pueden aplicarse directamente a otros cuerpos celestes. AnalogX implementa una separación explícita:

### 2.1 Sistemas Terrestres
* **Sistema Global Geodésico:** WGS84 (`EPSG:4326`), con coordenadas elipsoidales (latitud, longitud en grados decimales).
* **Superficie Vertical de Referencia:** Geoide EGM96 (Earth Gravitational Model 1996), utilizado por NASADEM y SRTM para definir alturas ortométricas sobre el nivel medio del mar.
* **Proyección Cartográfica Métrica Local:** Universal Transversal de Mercator (UTM):
  * Salar de Uyuni: UTM Zona 19 Sur (`EPSG:32719`) o Zona 20 Sur (`EPSG:32720`).
  * Sol de Mañana y Sur Lípez: UTM Zona 19 Sur (`EPSG:32719`).
  * Permite medir distancias, perímetros de polígonos y pendientes en metros euclidianos sin distorsión angular significativa.

### 2.2 Sistemas Marcianos
* **Sistema de Referencia Geodésico Oficial:** IAU 2000 Mars Sphere / Ellipsoid (`IAU:49900` / `ESRI:104905`):
  * Radio ecuatorial: $R_e = 3396.19\text{ km}$.
  * Radio polar: $R_p = 3376.20\text{ km}$.
  * Aplanamiento: $f = 0.00589$.
* **Coordenadas Planetocéntricas vs Planetográficas:**
  * *Planetocéntricas (Estándar NASA PDS actual):* Longitudes de $0^\circ$ a $360^\circ$ hacia el Este; latitud medida desde el centro de masas del planeta.
  * Para Terra Sirenum: Latitud $38.8^\circ\text{ S} \equiv -38.8^\circ$; Longitud $221.0^\circ\text{ E}$ ($139.0^\circ\text{ W}$).
* **Datum Vertical Marciano:** Areoide MOLA (superficie equipotencial gravitacional media donde la presión atmosférica media histórica de referencia se fijó originalmente en 6.1 mbar). No existe correlación física ni altitudinal con el nivel del mar terrestre.

### 2.3 Regla de Transformación para la Comparación
$$z_{\text{relativo}}(x,y) = z(x,y) - \min_{(u,v) \in \text{Cuenca}} z(u,v)$$
Ambos modelos digitales de elevación (NASADEM en Tierra y MOLA en Marte) se procesan localmente para generar modelos de elevación relativa local ($z_{\text{rel}}$ en metros), cancelando por completo los sesgos de datum absoluto.

---

## 3. CAPA DE NORMALIZACIÓN Y HOMOGENEIZACIÓN CIENTÍFICA

Para evitar la comparación espuria de píxeles con resoluciones dispares (ej. píxel MOLA de 463 m vs píxel NASADEM de 30 m), el motor aplica:

1. **Remuestreo Espacial Controlado:**
   * Al comparar pendientes regionales de cuenca, el DEM de 30 m terrestre se agrega mediante convolución de promedio de área o remuestreo bilineal a la escala decamétrica o kilométrica de la cuenca receptora marciana.
   * Al comparar fracturas poligonales, se trabaja en el dominio de imágenes de muy alta resolución (HiRISE 0.25 m vs ortofotos/Sentinel-2 10 m), computando distribuciones estadísticas de tamaño de malla ($D_{\text{pol}}$) en lugar de comparación directa píxel a píxel.
2. **Desacoplamiento Dimensional:**
   Las propiedades morfológicas se expresan en índices adimensionales:
   * Pendiente ($\tan \theta$ o radianes).
   * Circularidad de la cuenca ($4\pi \cdot \text{Área} / \text{Perímetro}^2$).
   * Confinamiento topográfico relativo ($TCI$).

---

## 4. LEDGER DE EVIDENCIAS CIENTÍFICAS (EVIDENCE LEDGER)

Todas las observaciones e inferencias científicas se persisten en una estructura inmutable que exige los siguientes campos de integridad:
* `id`: Identificador único del registro de observación.
* `source_name`: Nombre de la agencia y catálogo emisor (ej. `NASA PDS Geosciences Node`).
* `source_url`: Enlace verificable a la fuente oficial o identificador DOI.
* `product_id`: Código de producto exacto del catálogo (ej. `PSP_003160_1410`, `NASADEM_HGT.001`).
* `acquisition_date`: Fecha de captura por el sensor (o fecha de publicación si es bibliográfica).
* `version`: Versión oficial del procesamiento del dato.
* `unit`: Unidad física canónica del Sistema Internacional o adimensional explícita.
* `spatial_resolution`: Resolución espacial con unidades (`"30m"`, `"463m"`, `"25cm"`).
* `crs_datum`: Sistema de referencia de coordenadas y datum vertical exacto.
* `processing_method`: Descripción del algoritmo o pipeline aplicado (ej. `Sen2Cor L2A`, `MOLA MEGDR bilineal`, `DCS Band 8-7-5`).
* `value`: Valor numérico o estructura de datos correspondiente.
* `quality_uncertainty`: Desviación típica, error instrumental o margen de incertidumbre documentado.
* `verification_status`: Estado científico estrictamente tipado (`verificado_con_fuente`, `inferencia_razonable`, `hipotesis`, `pendiente_de_verificar`).

---

## 5. ORGANIZACIÓN MODULAR DEL SOFTWARE (`analogx-backend`)

```
backend_analogX/
├── app/
│   ├── main.py                     # Entrypoint de FastAPI y configuración de middleware CORS
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py               # Variables de entorno y configuración general Pydantic
│   ├── models/
│   │   ├── __init__.py             # Exportador de modelos tipados
│   │   ├── dataset.py              # Fuentes científicas y catálogos de datasets
│   │   ├── region.py               # Regiones terrestres, marcianas y metadatos CRS
│   │   ├── observation.py          # Mediciones observadas con los 13 atributos requeridos
│   │   └── evidence.py             # Evidencias cualitativas, comparaciones y limitaciones
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           └── router.py           # Endpoints informativos v1 (metadatos, regiones, auditoría)
├── research/                       # Informes científicos y auditorías exhaustivas
│   ├── source_audit.md             # Auditoría de las 16 fuentes oficiales
│   ├── dataset_catalog.csv         # Catálogo de datasets con categorías estrictas
│   ├── earth_mars_comparability.md # Evaluación de comparabilidad Tierra-Marte
│   ├── bolivia_candidates.md       # Evaluación de Uyuni, Sol de Mañana y Lípez
│   ├── scientific_hypothesis.md    # Formulación formal de hipótesis comprobable
│   ├── research_backlog.md         # Backlog técnico y validaciones manuales
│   └── safe_data_access_verification.md # Guía de verificación segura de accesos
├── docs/
│   └── scientific-data-architecture.md  # Arquitectura del sistema y datums
├── tests/
│   ├── __init__.py
│   └── test_models.py              # Suite de pruebas unitarias Pydantic con datos reales
├── requirements.txt                # Dependencias Python
├── pyproject.toml                  # Configuración de empaquetado y herramientas
└── README.md                       # Documentación para desarrolladores (Windows / Linux)
```

