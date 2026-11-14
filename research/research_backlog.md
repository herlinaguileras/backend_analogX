# BACKLOG DE INVESTIGACIÓN Y VALIDACIONES MANUALES (FASE 0 -> FASE 1)
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `research/research_backlog.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Estatus:** Backlog activo  

---

## 1. SPIKES TÉCNICOS PREVIOS A FASE 1

### SPIKE-01: Ingesta y Lectura de Productos PDS3 / PDS4 en Python sin Dependencias Nativas Complejas
* **Objetivo:** Determinar la ruta más robusta para leer ficheros `.IMG` / `.LBL` de MOLA MEGDR y cubos THEMIS en Windows (VS Code) y Linux sin forzar la instalación completa de USGS ISIS (que no tiene soporte nativo en Windows).
* **Alternativas a evaluar:**
  * Opción A: GDAL con driver PDS habilitado (`osgeo.gdal`).
  * Opción B: Librería pura Python `pds4_tools` y `planetarypy`.
  * Opción C: Pre-procesar a Cloud-Optimized GeoTIFF (COG) en pipelines offline y servir GeoTIFFs normalizados al backend.
* **Criterio de éxito:** Script de Python de menos de 50 líneas capaz de abrir `MEGT90N000CB` o similar y extraer una matriz numpy con su georreferenciación planetocéntrica.

### SPIKE-02: Transformación de Proyecciones Planetarias IAU 2000 vs Web Mercator / WGS84
* **Objetivo:** Definir la estrategia de estandarización geoespacial para que el frontend (React / Leaflet / Cesium / MapLibre) pueda superponer capas marcianas y terrestres de forma comprensible sin distorsionar distancias métricas.
* **Alternativas a evaluar:**
  * Opción A: Mantener dos lienzos de visualización independientes (Globo Tierra WGS84 EPSG:4326 y Globo Marte IAU:Mars2000 Sphere).
  * Opción B: Proyectar ambos a coordenadas locales cartesianas métricas relativas (UTM local para Tierra; Equirrectangular Planetocéntrico centrado en el depósito para Marte).
* **Criterio de éxito:** Documento de convención cartográfica aprobado en `docs/scientific-data-architecture.md`.

### SPIKE-03: Automatización de Peticiones Asíncronas a NASA AppEEARS API
* **Objetivo:** Crear un cliente HTTP asíncrono en FastAPI / `httpx` que autentique con NASA Earthdata Login URS, envíe un polígono GeoJSON de Uyuni o Sol de Mañana, sondee periódicamente (`task status`) y descargue el paquete de muestras de NASADEM y MODIS LST sin bloquear el hilo principal.
* **Criterio de éxito:** Pruebas unitarias de integración simuladas (mock) y reales con credenciales de entorno.

### SPIKE-04: Extracción de Bandas Espectrales SWIR en Copernicus CDSE vía STAC API
* **Objetivo:** Descargar exclusivamente las bandas B03 (Verde), B11 (SWIR-1) y B12 (SWIR-2) de Sentinel-2 L2A sobre Uyuni y Lípez sin tener que descargar el paquete SAFE completo de 1 GB.
* **Alternativas:** Uso de URLs firmadas de activos individuales en CDSE S3 o STAC asset stream con range requests HTTP.
* **Criterio de éxito:** Reducción del ancho de banda requerido de 1.1 GB a menos de 90 MB por observación.

---

## 2. VERIFICACIONES MANUALES OBLIGATORIAS ANTES DE LA FASE 1

| ID Tarea | Recurso | Descripción de la Verificación Manual | Responsable / Rol | Estado |
|---|---|---|---|---|
| **MAN-01** | NASA Earthdata | Crear cuenta en `urs.earthdata.nasa.gov` y generar token de aplicación para AppEEARS y CMR Search | Ingeniero Backend | Pendiente de verificar |
| **MAN-02** | ESA CDSE | Registrar cuenta en `dataspace.copernicus.eu` y obtener credenciales OAuth2 (Client ID y Secret) | Ingeniero Backend | Pendiente de verificar |
| **MAN-03** | HiRISE PDS | Verificar disponibilidad de descarga directa del producto JP2 de `PSP_003160_1410` en el archivo de la Universidad de Arizona | Investigador Planetario | Verificado con fuente |
| **MAN-04** | THEMIS ASU | Comprobar enlace de descarga del mosaico DCS de bandas 8-7-5 para la cuadrícula de Terra Sirenum en el servidor de la ASU | Investigador Planetario | Verificado con fuente |
| **MAN-05** | SERGEOMIN Bolivia | Revisar mapas geológicos impresos/digitalizados del Altiplano Sur (Hojas Uyuni, San Pablo de Lípez) para verificar espesores de halita y travertinos | Investigador Geólogo | Inferencia razonable |
| **MAN-06** | MOLA PDS | Descargar tile regional de MEG128 correspondiente a latitudes 30°S-45°S y longitudes 200°E-240°E para pruebas locales | Ingeniero SIG | Pendiente de verificar |

---

## 3. HISTORIAS DE USUARIO PARA FASE 1 (BACKEND SPRINT)

* **HU-01: Ingesta de Metadatos de Regiones (Catalog Service):**
  Como usuario del sistema, quiero consultar los metadatos oficiales de las regiones análogas terrestres y planetarias (Uyuni, Sol de Mañana, Terra Sirenum) con su sistema de referencia, coordenadas bounding box y fuentes bibliográficas.
* **HU-02: Endpoint de Variables Físicas Comparadas:**
  Como investigador, quiero obtener una matriz estructurada que exponga las variables comparables (pendiente, rugosidad, diámetro de polígonos, índices de salinidad) con sus unidades, resoluciones, método de procesamiento e incertidumbres.
* **HU-03: Ledger de Evidencias Científicas (Evidence Vault):**
  Como evaluador del NASA Space Apps Challenge, quiero auditar las limitaciones científicas y la trazabilidad de cada medición para asegurar que no existan valores ficticios ni extrapolaciones no justificadas.
* **HU-04: Generador de Perfiles de Elevación Normalizados:**
  Como científico de datos, quiero solicitar un transecto topográfico de cuenca que normalice el relieve relativo ($z - z_{\min}$) para superponer el perfil de Terra Sirenum con el del Salar de Uyuni en una misma gráfica comparativa.

