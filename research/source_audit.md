# AUDITORÍA CIENTÍFICA Y TÉCNICA DE FUENTES OFICIALES (16 RECURSOS)
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `research/source_audit.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Fecha:** Noviembre 2026  
> **Estatus:** Auditoría exhaustiva completada  
> **Regla de integridad:** Ningún atributo se asume público o sin autenticación por el mero hecho de contar con una interfaz web. Los atributos no verificables de forma autónoma quedan consignados explícitamente como `"no verificado"`.

---

## 1. MATRIZ RESUMEN DE CLASIFICACIÓN DE LAS 16 FUENTES

| # | Recurso / Repositorio | Agencia | Instrumento / Misión | Tipo Primario | Nivel de Verificación | Prioridad AnalogX |
|---|-----------------------|---------|-----------------------|---------------|-----------------------|-------------------|
| 1 | [Earthdata Search](https://search.earthdata.nasa.gov/) | NASA | Múltiples (EOSDIS/CMR) | Catálogo federado / API | Verificado con fuente | **MVP** |
| 2 | [NASA Worldview](https://worldview.earthdata.nasa.gov/) | NASA | GIBS (Terra, Aqua, etc.) | Visualización / WMTS | Verificado con fuente | **MVP** (UI/Contexto) |
| 3 | [Planetary Data System (PDS)](https://pds.nasa.gov/) | NASA | Nodos Geosciences/Imaging | Repositorio científico planetario | Verificado con fuente | **MVP** |
| 4 | [Lunar Reconnaissance Orbiter (LRO)](https://pds-geosciences.wustl.edu/missions/lro/) | NASA | LROC, LOLA, Diviner, Mini-RF | Misión lunar / Archivo PDS | Verificado con fuente | **Segunda fase** |
| 5 | [LRO Diviner](https://pds-geosciences.wustl.edu/missions/lro/diviner.htm) | NASA | Radiómetro térmico Diviner | Radiometría infrarroja lunar | Verificado con fuente | **Segunda fase** |
| 6 | [NASA AppEEARS](https://appeears.earthdatacloud.nasa.gov/) | NASA | LP DAAC (MODIS, NASADEM, etc.) | Extractor de análisis (ARD) / API | Verificado con fuente | **MVP** |
| 7 | [MOLA (Mars Orbiter Laser Altimeter)](https://pds-geosciences.wustl.edu/missions/mgs/mola.html) | NASA | Mars Global Surveyor (MGS) | Altimetría láser marciana | Verificado con fuente | **MVP** |
| 8 | [CRISM (Compact Reconnaissance Imaging Spectrometer)](https://pds-geosciences.wustl.edu/missions/mro/crism.htm) | NASA | Mars Reconnaissance Orbiter | Espectrometría VNIR-SWIR marciana | Verificado con fuente | **MVP** |
| 9 | [RADARSAT Constellation (RCM)](https://donnees-data.asc-csa.gc.ca/en/dataset/rcm) | CSA | RCM 1, 2, 3 (Banda C SAR) | Radar orbital polarimétrico | Verificado con fuente | **Segunda fase** |
| 10 | [RADARSAT-1](https://donnees-data.asc-csa.gc.ca/en/dataset/radarsat1) | CSA | RADARSAT-1 (Banda C SAR) | Archivo histórico SAR (1995-2013) | Verificado con fuente | **Descartado** |
| 11 | [SAR Python Tutorial](https://github.com/asc-csa/Synthetic_Aperture_Radar_Tutorial) | CSA | Código / Algoritmos SAR | Tutorial metodológico / Código abierto | Verificado con fuente | **MVP** (Algoritmos) |
| 12 | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) | ESA | Sentinel-1, Sentinel-2, COP-DEM | Misiones Sentinel / API OData-STAC | Verificado con fuente | **MVP** |
| 13 | [Open Science Catalog](https://opensciencedata.esa.int/) | ESA | Proyectos de investigación ESA | Catálogo temático STAC | Verificado con fuente | **Segunda fase** |
| 14 | [JAXA G-Portal](https://www.gportal.jaxa.jp/?lang=en) | JAXA | ALOS PALSAR, AW3D30, GCOM | Observación terrestre (Banda L/DEM) | Verificado con fuente | **Segunda fase** |
| 15 | [NASA — Bolivian Salt Flats](https://science.nasa.gov/earth/earth-observatory/bolivian-salt-flats-151813/) | NASA | Earth Observatory (MODIS/Landsat) | Publicación científica / Calibración | Verificado con fuente | **MVP** (Línea base) |
| 16 | [NASA — Chloride Salt Deposit Mars](https://science.nasa.gov/resource/chloride-salt-deposit-in-southern-highlands-of-mars-annotated/) | NASA | Mars Odyssey (THEMIS) / MRO (HiRISE)| Publicación y productos anotados | Verificado con fuente | **MVP** (Objetivo Marte)|

---

## 2. AUDITORÍA DETALLADA RECURSO POR RECURSO

### Recurso 1: NASA Earthdata Search
* **Agencia responsable:** NASA (Earth Science Data and Information System - EOSDIS).
* **Instrumento / Misión / Catálogo:** Catálogo federado EOSDIS Core System (ECS) basado en el Common Metadata Repository (CMR). Indexa instrumentos como MODIS, ASTER, MISR, VIIRS, SRTM, GEDI, ICESat-2, ECOSTRESS, OLI (Landsat).
* **Variables disponibles:** Reflectancia superficial (VNIR/SWIR), temperatura superficial de la tierra (LST), modelos digitales de elevación (DEM), índices de vegetación/salinidad, humedad de suelo, contenido de vapor de agua atmosférico y aerosoles.
* **Cobertura geográfica:** Global terrestre (-90° a +90° Latitud, -180° a +180° Longitud).
* **Resolución espacial:** Heterogénea según sensor: desde 15 m (ASTER VNIR), 30 m (NASADEM, Landsat HLS), 70 m (ECOSTRESS), 250 m a 1 km (MODIS/VIIRS), hasta 0.25° a 1° (modelos climáticos MERRA-2).
* **Cobertura temporal:** Década de 1970 hasta la actualidad (frecuencias diaria, compuesta de 8/16 días y estacional).
* **Formatos disponibles:** Cloud-Optimized GeoTIFF (COG), GeoTIFF, HDF-EOS (HDF4/HDF5), NetCDF-4, Flat binary (.hgt).
* **Disponibilidad de API o descarga:** 
  * *Búsqueda:* API CMR Search pública y abierta (`https://cmr.earthdata.nasa.gov/search/granules.json`).
  * *Descarga:* Acceso HTTP/S3 directo a través de los servidores de cada DAAC (LP DAAC, GES DISC, NSIDC). Requiere invocación con cabecera de autenticación.
* **Requisitos de autenticación:** Cuenta gratuita obligatoria en **NASA Earthdata Login (URS)**. Para consumo mediante API/CLI se requieren tokens OAuth Bearer o archivo de credenciales `~/.netrc`.
* **Licencia:** NASA Open Data Policy (dominio público gubernamental estadounidense, redistribución y uso científico/comercial sin costo).
* **Tamaño aproximado del producto:** Gránulos individuales desde 15 MB (baldosas NASADEM 1°x1°) hasta 500 MB - 1.5 GB (escenas completas HDF de MODIS o ASTER).
* **Complejidad de procesamiento:** **Media a Alta**. Requiere desempaquetado de sub-datasets HDF/NetCDF, reproyección desde proyección sinusoidal o UTM a sistemas canónicos, y enmascaramiento de nubes y valores nulos (*fill values*).
* **Limitaciones de calidad:** Vacíos por presencia de nubes densas en sensores ópticos; artefactos de sombra en zonas de alta pendiente montañosa; sesgos por humedad superficial transitoria en salares.
* **Utilidad específica para AnalogX:** Motor central para consultar y descargar el modelo digital de elevación terrestre (NASADEM_HGT) sobre el Salar de Uyuni y la región volcánica de Lípez / Sol de Mañana.
* **Prioridad:** **MVP**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 2: NASA Worldview
* **Agencia responsable:** NASA (EOSDIS / Global Imagery Browse Services - GIBS).
* **Instrumento / Misión / Catálogo:** Satélites Terra, Aqua, Suomi NPP, NOAA-20/21, Landsat, Sentinel-2 (vía agregación GIBS).
* **Variables disponibles:** Imágenes diarias de reflectancia corregida en color verdadero (Bands 1-4-3 o equivalentes) y falso color (Bands 7-2-1 para realce de agua, nieve e hidrocarburos/evaporitas), anomalías térmicas (incendios/geotermia), aerosoles, nubes.
* **Cobertura geográfica:** Global terrestre completa.
* **Resolución espacial:** Resolución visual de visualización entre 250 m (MODIS/VIIRS) y 30 m (mosaicos Landsat/Sentinel). No almacena los números digitales originales completos de 16 bits.
* **Cobertura temporal:** Desde mayo del 2000 (Terra MODIS) hasta tiempo casi real (*Near Real-Time - NRT*, retraso de 3 horas respecto a la adquisición).
* **Formatos disponibles:** Mosaicos web WMTS/WMS (formatos raster PNG/JPEG), exportación de GeoTIFF georreferenciado de visualización.
* **Disponibilidad de API o descarga:** API GIBS WMTS pública y abierta (`https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/...`). No requiere API Key para llamadas de visualización por tiles.
* **Requisitos de autenticación:** Ninguno para visualización y consumo de capas WMTS.
* **Licencia:** NASA Open Data Policy (dominio público).
* **Tamaño aproximado del producto:** Baldosas ligeras de 256x256 píxeles (~20 a 60 KB por baldosa).
* **Complejidad de procesamiento:** **Baja**. Diseñado para consumo directo en bibliotecas frontend como Leaflet, OpenLayers, Cesium o MapLibre.
* **Limitaciones de calidad:** Es un producto de inspección (*browse product*) con compresión visual y estiramiento radiométrico no lineal aplicado; **NO es apto para cálculos espectroscópicos cuantitativos ni inversión de modelos de reflectancia**.
* **Utilidad específica para AnalogX:** Validación visual rápida del estado de inundación estacional del Salar de Uyuni antes de seleccionar fechas de análisis espectral, y visualización de capas base en el frontend.
* **Prioridad:** **MVP** (como servicio de soporte visual y contexto).
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 3: NASA Planetary Data System (PDS)
* **Agencia responsable:** NASA (Planetary Science Division). Nodos relevantes: Geosciences Node (Washington University in St. Louis - WUSTL), Imaging / Cartography Node (USGS Astrogeology / JPL), Atmospheres Node (NMSU).
* **Instrumento / Misión / Catálogo:** Archivo maestro de todas las misiones planetarias de la NASA: Mars Global Surveyor (MGS), Mars Odyssey, Mars Reconnaissance Orbiter (MRO), Mars Exploration Rovers (MER Spirit/Opportunity), Mars Science Laboratory (Curiosity), Mars 2020 (Perseverance), Lunar Reconnaissance Orbiter (LRO), Magellan, etc.
* **Variables disponibles:** Altimetría láser de pulso y mallas interpoladas (MOLA, LOLA), cubos hiperespectrales VNIR-SWIR (CRISM), imágenes térmicas y emisividad infrarroja (THEMIS), imágenes monocromáticas y de color de resolución submétrica (HiRISE, CTX, LROC NAC/WAC), gravimetría y radar de penetración subsuperficial (SHARAD, MARSIS).
* **Cobertura geográfica:** Superficie completa de cuerpos planetarios explorados (Marte, Luna, Mercurio, etc.).
* **Resolución espacial:** Desde decenas de kilómetros (primeras misiones) hasta 0.25 m/px (HiRISE) y 0.5 m/px (LROC NAC).
* **Cobertura temporal:** Década de 1970 hasta la actualidad (misiones activas actualizadas por liberaciones programadas cada 3 a 6 meses).
* **Formatos disponibles:** Estándares PDS3 (ficheros de datos `.IMG` / `.DAT` acompañados de ficheros de cabecera `.LBL` en texto ASCII) y PDS4 (ficheros binarios o FITS estructurados acompañados de esquemas XML de metadatos `.xml`). Productos procesados en GeoTIFF e ISIS cube (`.cub`).
* **Disponibilidad de API o descarga:** 
  * API unificada PDS (`https://pds.nasa.gov/api/`).
  * WUSTL Orbital Data Explorer (ODE) REST API (`https://oderest.rsl.wustl.edu/live2/`): permite consultas espaciales filtradas por producto, coordenadas planetocéntricas y fecha.
  * Servidores HTTPS y SFTP abiertos para descarga directa de los volúmenes de datos.
* **Requisitos de autenticación:** Acceso público universal y gratuito. No requiere registro ni autenticación para consulta o descarga HTTP.
* **Licencia:** Dominio público (NASA Planetary Science Open Data).
* **Tamaño aproximado del producto:** Gránulos individuales desde 500 KB (archivos tabulares de pulso láser) hasta 1 a 3 GB por cubo crudo CRISM o escena ortorrectificada HiRISE RDR.
* **Complejidad de procesamiento:** **Crítica a Alta**. Los formatos PDS3/PDS4 requieren software especializado (USGS ISIS3/ISIS4, librerías Python como `pds4_tools`, `planetarypy`, GDAL con soporte PDS habilitado). Las proyecciones planetocéntricas/planetográficas y los datums esferoidales marcianos (radio 3396.19 km) deben transformarse cuidadosamente para evitar distorsiones métricas severas.
* **Limitaciones de calidad:** Ruido instrumental en detectores térmicos e infrarrojos; franjas de artefactos de calibración (*striping*); variabilidad por tormentas globales de polvo en Marte; calibración fotométrica compleja en función del ángulo de fase solar.
* **Utilidad específica para AnalogX:** Repositorio canónico e irremplazable de donde se extraen los datos oficiales de Terra Sirenum (MOLA, THEMIS, CRISM, HiRISE).
* **Prioridad:** **MVP**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 4: Lunar Reconnaissance Orbiter (LRO)
* **Agencia responsable:** NASA (Goddard Space Flight Center) y PDS Geosciences / Imaging Nodes.
* **Instrumento / Misión / Catálogo:** Lunar Reconnaissance Orbiter (LRO). Instrumentos principales: Lunar Orbiter Laser Altimeter (LOLA), Lunar Reconnaissance Orbiter Camera (LROC - WAC y NAC), Diviner Lunar Radiometer Experiment, Lunar Exploration Neutron Detector (LEND), Miniature Radio Frequency (Mini-RF).
* **Variables disponibles:** Altimetría topográfica lunar, pendientes locales, rugosidad superficial (desviación típica de pendientes basales de pulso LOLA), reflectancia visible (albedo a escala métrica), temperatura superficial e inercia térmica diurna/nocturna (Diviner).
* **Cobertura geográfica:** Global lunar (-90° a +90° latitud selenográfica). Cobertura densa en latitudes polares debido a la órbita cuasi-polar.
* **Resolución espacial:** 
  * LOLA Gridded Data Record (LDEM): 512 píxeles por grado (~59 m/px en el ecuador, hasta 10-20 m/px en polos).
  * LROC WAC: 100 m/px multiespectral.
  * LROC NAC: 0.5 a 2 m/px pancromático.
* **Cobertura temporal:** Junio 2009 hasta el presente.
* **Formatos disponibles:** PDS3 (`.IMG`/`.LBL`), PDS4 (`.xml`/`.dat`), GeoTIFF (mediante USGS Astrogeology y WUSTL Lunar ODE).
* **Disponibilidad de API o descarga:** Lunar Orbital Data Explorer (Lunar ODE) REST API y descargas HTTPS directas en el nodo Geosciences de WUSTL.
* **Requisitos de autenticación:** Libre y público, sin registro ni credenciales.
* **Licencia:** Dominio público.
* **Tamaño aproximado del producto:** Desde 100 MB hasta varios gigabytes por cuadrante de mosaico DEM o imagen NAC no comprimida.
* **Complejidad de procesamiento:** **Alta**. Requiere proyecciones estereográficas polares lunares o cilíndricas equidistantes, y datum esférico lunar de radio medio $R_L = 1737.4\text{ km}$.
* **Limitaciones de calidad:** Sombras permanentes (*Permanently Shadowed Regions - PSRs*) en cráteres polares donde los sensores ópticos no captan señal reflejada (dependencia de LOLA y LAMP); gradientes térmicos extremos de más de 300 K entre el día y la noche lunar.
* **Utilidad específica para AnalogX:** Provee la base de datos de calibración para la futura expansión lunar del motor (evaluación de análogos de rugosidad en regolito y cráteres de impacto terrestres en el Altiplano).
* **Prioridad:** **Segunda fase** (El MVP de AnalogX se centra en la hipótesis de depósitos de cloruro marcianos vs evaporitas bolivianas).
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 5: LRO Diviner (Lunar Radiometer Experiment)
* **Agencia responsable:** NASA (UCLA / JPL / PDS Geosciences Node).
* **Instrumento / Misión / Catálogo:** Diviner Lunar Radiometer Experiment (radiómetro multicanal de 9 filtros espectrales a bordo de LRO).
* **Variables disponibles:** Temperatura de brillo infrarrojo ($T_b$), mapas derivados de temperatura diurna y nocturna, inercia térmica del regolito, y posición de la banda del rasgo Christiansen (*Christiansen Feature - CF* a ~8 µm) para inferir polímeros de sílice y contenido composicional de plagioclasas/piroxenos.
* **Cobertura geográfica:** Global lunar (-90° a +90°).
* **Resolución espacial:** Global Gridded Data Records (GDR) a resoluciones de 0.5° (~15 km), 128 px/deg (~240 m/px) en regiones polares y perfiles de traza de órbita.
* **Cobertura temporal:** Julio 2009 hasta el presente.
* **Formatos disponibles:** Tablas ASCII/binarias PDS3 (RDR), archivos binarios gridded con cabecera PDS (`.TAB`, `.DAT`, `.LBL`), GeoTIFF en repositorios procesados de UCLA.
* **Disponibilidad de API o descarga:** Portal Diviner UCLA (`https://www.diviner.ucla.edu/`) y archivo PDS Geosciences. Consultas programáticas vía Lunar ODE REST API.
* **Requisitos de autenticación:** Libre y público, sin autenticación.
* **Licencia:** Dominio público.
* **Tamaño aproximado del producto:** Cientos de gigabytes en datos brutos tabulares RDR; productos integrados GDR de 50 a 300 MB por mapa temático.
* **Complejidad de procesamiento:** **Alta a Crítica** para procesar calibraciones de ángulo de emisión y normalización térmica diurna; **Media** si se consumen mapas GDR compilados.
* **Limitaciones de calidad:** Fuerte anisotropía térmica por rugosidad superficial submétrica (efecto de cavidad en rocas y sombras de rocas); el rasgo Christiansen se desplaza en función del ángulo de fase solar y el tamaño de grano del regolito.
* **Utilidad específica para AnalogX:** Modelo de comparación térmica infrarroja para análogos lunares de inercia térmica en depósitos piroclásticos y suelos áridos.
* **Prioridad:** **Segunda fase**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 6: NASA AppEEARS
* **Agencia responsable:** NASA (Distributed Active Archive Center for Land Processes - LP DAAC / USGS EROS).
* **Instrumento / Misión / Catálogo:** Servicio de extracción federado que integra colecciones de MODIS (Terra/Aqua), VIIRS, ECOSTRESS, SMAP, NASADEM, SRTM, HLS (Harmonized Landsat-Sentinel) y ASTER GED.
* **Variables disponibles:** Extracción puntual o vectorial de series temporales de reflectancia superficial, temperatura y emisividad terrestre (LST), evapotranspiración, índices de vegetación (NDVI, EVI), humedad superficial de suelo, y elevación/pendiente topográfica.
* **Cobertura geográfica:** Cobertura global terrestre de las misiones soportadas.
* **Resolución espacial:** Desde 30 m (NASADEM, HLS, SRTM), 70 m (ECOSTRESS), hasta 250 m - 1 km (MODIS, VIIRS, SMAP).
* **Cobertura temporal:** 2000 hasta el presente (varía por producto; datos históricos SRTM año 2000, MODIS desde 2000, ECOSTRESS desde 2018).
* **Formatos disponibles:** Paquetes *Analysis Ready Data (ARD)*: GeoTIFF georreferenciados, NetCDF-4, y tablas CSV para series temporales puntuales.
* **Disponibilidad de API o descarga:** AppEEARS REST API completa (`https://appeears.earthdatacloud.nasa.gov/api/`). Permite autenticación, consulta de productos, envío de tareas asíncronas de extracción vectorial (GeoJSON), sondeo de estado y descarga directa del archivo ZIP procesado.
* **Requisitos de autenticación:** Cuenta obligatoria en **NASA Earthdata Login**. Autenticación vía API mediante endpoint `/api/login` enviando credenciales básicas para obtener un Bearer Token JWT temporal.
* **Licencia:** NASA Open Data Policy.
* **Tamaño aproximado del producto:** Muy eficiente y compacto: desde unos pocos kilobytes (CSV puntual) hasta 10-80 MB (recorte espacial exacto en GeoTIFF del polígono de interés).
* **Complejidad de procesamiento:** **Baja a Media**. Los datos se entregan recortados por el área de interés (AOI), reproyectados al sistema de referencia solicitado, con máscaras de calidad asociadas y factores de escala documentados.
* **Limitaciones de calidad:** El procesamiento es asíncrono en la infraestructura en la nube de la NASA; las solicitudes pueden tardar desde 2 minutos hasta varias horas según la carga del cluster; no es viable para respuestas instantáneas síncronas en tiempo real sin una capa de persistencia previa.
* **Utilidad específica para AnalogX:** Herramienta óptima para extraer muestras vectorizadas de NASADEM, LST y series temporales biofísicas sobre las coordenadas del Salar de Uyuni y Sol de Mañana sin necesidad de descargar escenas completas de varios gigabytes.
* **Prioridad:** **MVP**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 7: MOLA (Mars Orbiter Laser Altimeter)
* **Agencia responsable:** NASA (Goddard Space Flight Center) / PDS Geosciences Node en WUSTL.
* **Instrumento / Misión / Catálogo:** Mars Global Surveyor (MGS) - Mars Orbiter Laser Altimeter (MOLA).
* **Variables disponibles:** Elevación topográfica planetaria referenciada al Areoide marciano (geoide gravitacional equipotencial medio), rugosidad superficial a escala de línea de base (desviación típica del ancho de pulso reflejado a 1064 nm), reflectancia de pulso activo.
* **Cobertura geográfica:** Global marciano (-90° a +90° latitud planetocéntrica). Espaciamiento de órbitas de ~2-3 km en el ecuador, convergiendo a submétrico en los polos.
* **Resolución espacial:** 
  * Mission Experiment Gridded Data Records (MEGDR): 4, 16, 32, 64 y 128 píxeles por grado. La versión de máxima resolución (`MEG128`) posee un tamaño de píxel de aproximadamente **463 metros por píxel** en el ecuador marciano (~0.0078125° por píxel).
  * Precision Experiment Data Records (PEDR): huella láser puntual individual de ~300 m de diámetro espaciada cada 150 m a lo largo de la traza orbital.
* **Cobertura temporal:** Fase de mapeo orbital principal de MGS (1997 a 2001).
* **Formatos disponibles:** PDS3 (`.IMG`/`.LBL`), tablas binarias PEDR, y productos reproyectados en GeoTIFF disponibles en USGS Astrogeology y WUSTL ODE.
* **Disponibilidad de API o descarga:** Directorios HTTPS/FTP directos en PDS Geosciences Node (`https://pds-geosciences.wustl.edu/mgs/mgs-m-mola-5-megdr-l3-v1/`). Integrado en WUSTL ODE REST API.
* **Requisitos de autenticación:** Acceso público universal sin autenticación ni registro.
* **Licencia:** Dominio público.
* **Tamaño aproximado del producto:** El mosaico global completo `MEG128` en entero de 16 bits ocupa ~1.8 GB descomprimido. Los cuadrantes regionales de 45°x45° ocupan entre 60 y 140 MB en formato comprimido.
* **Complejidad de procesamiento:** **Media**. Requiere aplicar el factor de escala y offset oficial ($Elevación = DN \times Escala + Offset$) y manejar el datum Areoide MOLA con radio ecuatorial de 3396.0 km y sistema de coordenadas planetocéntricas con longitudes 0° a 360° Este.
* **Limitaciones de calidad:** La resolución de 463 m/px es apta para caracterización morfométrica regional y de cuenca, pero **NO resuelve micro-rugosidad submétrica ni micro-canales**; la cuadrícula ecuatorial incluye interpolación entre trazas orbitales adyacentes; no debe compararse su valor absoluto con elevaciones terrestres referenciadas al nivel medio del mar (EGM96).
* **Utilidad específica para AnalogX:** Fuente canónica para extraer la topografía regional, pendiente de cuenca y relieve relativo de la depresión de Terra Sirenum (~38.8° S, 221° E).
* **Prioridad:** **MVP**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 8: CRISM (Compact Reconnaissance Imaging Spectrometer for Mars)
* **Agencia responsable:** NASA (Johns Hopkins University Applied Physics Laboratory - JHU/APL) / PDS Geosciences Node.
* **Instrumento / Misión / Catálogo:** Mars Reconnaissance Orbiter (MRO) - CRISM.
* **Variables disponibles:** Espectroscopía de reflectancia I/F corregida en el rango visible/infrarrojo cercano (VNIR: 0.36 a 1.05 µm) e infrarrojo de onda corta (SWIR: 1.00 a 3.92 µm en 544 canales); cubos de parámetros espectrales de resumen (mapas de absorción de agua, minerales hidratados, filosilicatos/arcillas esmectitas, sulfatos polihidratados/monohidratados, carbonatos y rasgos de sales).
* **Cobertura geográfica:** Modo multiespectral de baja resolución (MRDR) con cobertura cuasi-global (~200 m/px); modo hiperespectral dirigido de alta resolución (FRT, HRL, HRS) con cobertura extremadamente dispersa y específica (~3-4% de la superficie marciana).
* **Resolución espacial:** ~18 m/px (FRT - Full Resolution Targeted), ~36 m/px (HRL - Half Resolution Long), ~200 m/px (MRDR).
* **Cobertura temporal:** 2006 a 2023 (el sistema de enfriamiento criogénico de los detectores SWIR se agotó en 2017; las observaciones con canales SWIR plenamente operativos corresponden al periodo 2006-2017).
* **Formatos disponibles:** Formatos PDS3 (`.IMG`/`.LBL`), cubos hiperespectrales ENVI (`.dat`/`.hdr`), y productos derivados ortorrectificados MTRDR (Map-projected Targeted Reduced Data Records).
* **Disponibilidad de API o descarga:** WUSTL CRISM Spectral Library y ODE REST API. Servidores HTTPS directos en PDS Geosciences.
* **Requisitos de autenticación:** Acceso público universal sin autenticación.
* **Licencia:** Dominio público.
* **Tamaño aproximado del producto:** Un gránulo FRT crudo ocupa entre 500 MB y 2.5 GB. Los productos de parámetros de resumen MTRDR procesados ocupan entre 40 y 180 MB.
* **Complejidad de procesamiento:** **Crítica**. Los cubos crudos requieren calibración radiométrica, eliminación de ruido térmico y de detector (*destriping*), modelado y remoción de la absorción de CO2 atmosférico marciano (método *volcano scan* o modelado DISORT), y fotometría. Para AnalogX se deben utilizar exclusivamente los productos de parámetros derivados MTRDR o compilaciones validadas en literatura.
* **Limitaciones de calidad:** **Firma espectral de cloruros:** El cloruro de sodio (halita) y otros cloruros anhidros son espectralmente transparentes o "planos" (carentes de bandas de absorción diagnósticas profundas) en el rango VNIR-SWIR de CRISM (1.0 - 2.5 µm); no se identifican por picos de absorción propios en CRISM, sino por una pendiente espectral ligeramente positiva (*red-sloped*), carencia de bandas de agua y sulfatos, y por su asociación espacial con detecciones térmicas de THEMIS y morfología HiRISE.
* **Utilidad específica para AnalogX:** Comprobación del contexto mineralógico de Terra Sirenum (descarte de sulfatos masivos o verificación de arcillas/filosilicatos estratigráficamente inferiores sobre los que se depositaron los cloruros).
* **Prioridad:** **MVP** (utilizando parámetros MTRDR documentados e interpretaciones bibliográficas verificadas).
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 9: CSA RADARSAT Constellation Mission (RCM)
* **Agencia responsable:** Canadian Space Agency (CSA / ASC).
* **Instrumento / Misión / Catálogo:** Constelación RADARSAT (RCM 1, RCM 2, RCM 3; tres satélites SAR en órbita heliosincrónica a 600 km de altitud).
* **Variables disponibles:** Radar de apertura sintética (SAR) en Banda C (frecuencia central 5.405 GHz, longitud de onda $\lambda \approx 5.55\text{ cm}$). Coeficientes de retrodispersión normalizados ($\sigma^0$, $\gamma^0$), polarimetría compacta (*circular-transmit, linear-receive* generando productos Stokes $S_0, S_1, S_2, S_3$), descomposición $m-\chi$.
* **Cobertura geográfica:** Prioridad de vigilancia sobre territorio y costas canadienses; cobertura global terrestre y marítima sujeta a planes de adquisición por cuotas de misión.
* **Resolución espacial:** Modo Spotlight (1 m), Very High Resolution (3 m), High Resolution (5 m), Medium Resolution (16 m o 30 m), Low Resolution / ScanSAR (50 m o 100 m).
* **Cobertura temporal:** Junio 2019 hasta el presente.
* **Formatos disponibles:** Paquetes SAR estándar CEOS / SAFE (GeoTIFF o NITF acompañados de metadatos XML de órbita y calibración).
* **Disponibilidad de API o descarga:** Earth Observation Data Management System (EODMS - `https://www.eodms-sgdot.nrcan-rncan.gc.ca/`) del Gobierno de Canadá, con servicio REST API documentado.
* **Requisitos de autenticación:** Cuenta obligatoria registrada y validada en EODMS. Las imágenes de muy alta resolución (<5 m) están restringidas por la Ley de Sistemas de Teledetección Espacial de Canadá a usuarios gubernamentales o académicos autorizados; las resoluciones medianas (16m-30m) son accesibles con cuenta estándar aprobada.
* **Licencia:** Open Government Licence - Canada (con cláusulas específicas para control de difusión de alta resolución).
* **Tamaño aproximado del producto:** 300 MB a 3 GB por escena procesada (SLC / GRD).
* **Complejidad de procesamiento:** **Alta**. Requiere corrección Doppler, calibración radiométrica de la matriz de dispersión, corrección de terreno (*Range-Doppler Terrain Correction*) empleando un DEM externo (NASADEM o COP30) y filtrado de ruido moteado (*speckle*).
* **Limitaciones de calidad:** El catálogo de adquisiciones sobre el Altiplano boliviano (Salar de Uyuni y Lípez) es esporádico y no sistemático en comparación con la cobertura de Sentinel-1 de la ESA; tiempos de aprobación de cuenta y límites de cuota de descarga para usuarios fuera de Canadá.
* **Utilidad específica para AnalogX:** Estudio avanzado de retrodispersión y polarimetría compacta en costras de sal para caracterizar rugosidad dieléctrica.
* **Prioridad:** **Segunda fase** (Sentinel-1 de la ESA cubre la misma banda C con acceso irrestricto y mayor frecuencia en Bolivia).
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 10: CSA RADARSAT-1
* **Agencia responsable:** Canadian Space Agency (CSA / ASC).
* **Instrumento / Misión / Catálogo:** Satélite RADARSAT-1 (sensor SAR Banda C a 5.3 GHz).
* **Variables disponibles:** Amplitud de retrodispersión de microondas en polarización única horizontal fija (HH).
* **Cobertura geográfica:** Archivo histórico global de campañas de adquisición específicas.
* **Resolución espacial:** Desde 8 m (Fine mode), 25-30 m (Standard mode), hasta 50-100 m (ScanSAR).
* **Cobertura temporal:** Noviembre 1995 a Marzo 2013 (misión finalizada).
* **Formatos disponibles:** Formato CEOS heredado (ficheros binarios de radar con descriptores de texto plano ASCII) y GeoTIFF procesados en colecciones de datos abiertos de Canadá.
* **Disponibilidad de API o descarga:** Descarga a través del portal EODMS y archivo histórico de datos abiertos de RADARSAT-1 del gobierno de Canadá.
* **Requisitos de autenticación:** Cuenta registrada en EODMS.
* **Licencia:** Open Government Licence - Canada.
* **Tamaño aproximado del producto:** 150 MB a 600 MB por escena.
* **Complejidad de procesamiento:** **Alta**. Formatos antiguos CEOS que presentan incompatibilidades con librerías GIS directas sin herramientas de conversión (ESA SNAP, GDAL legacy CEOS driver). Polarización simple sin capacidad polarimétrica.
* **Limitaciones de calidad:** Sensor histórico sin adquisiciones contemporáneas; calibración radiométrica desfasada respecto a constelaciones modernas; polarización exclusivamente HH; adquisiciones limitadas sobre el Altiplano boliviano en las décadas de 1990 y 2000.
* **Utilidad específica para AnalogX:** Análisis multitemporal retrospectivo de la rugosidad del Salar de Uyuni hace 25 años. Carece de valor operativo directo frente a Sentinel-1.
* **Prioridad:** **Descartado** para el MVP y pipeline primario.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 11: CSA SAR Python Tutorial
* **Agencia responsable:** Canadian Space Agency (CSA / ASC).
* **Instrumento / Misión / Catálogo:** Repositorio público oficial de código abierto en GitHub (`asc-csa/Synthetic_Aperture_Radar_Tutorial`).
* **Variables disponibles:** Implementaciones en código Python de algoritmos fundamentales de radar: calibración radiométrica ($\beta^0, \sigma^0, \gamma^0$), conversión de amplitud a decibelios (dB), filtrado adaptativo de speckle (Lee, Frost, Kuan), polarimetría compacta, parámetros de Stokes ($S_0, S_1, S_2, S_3$), descomposición $m-\chi$ y clasificación no supervisada de rugosidad.
* **Cobertura geográfica:** Conjuntos de datos de muestra incluidos en el repositorio (zonas de prueba en Canadá).
* **Resolución espacial:** N/A (algoritmos matemáticos y scripts educativos).
* **Cobertura temporal:** Código mantenido y actualizado en GitHub (2020 a 2026).
* **Formatos disponibles:** Jupyter Notebooks (`.ipynb`), scripts modulares en Python (`.py`), archivos de prueba GeoTIFF y HDF5.
* **Disponibilidad de API o descarga:** Repositorio Git público (`git clone https://github.com/asc-csa/Synthetic_Aperture_Radar_Tutorial.git`) o descarga directa como archivo ZIP desde GitHub.
* **Requisitos de autenticación:** Ninguno (acceso público abierto).
* **Licencia:** MIT License / Open Source (reutilización y modificación permitida para proyectos científicos y comerciales).
* **Tamaño aproximado del producto:** < 120 MB incluyendo datos raster de muestra.
* **Complejidad de procesamiento:** **Baja**. Ejecución directa mediante librerías científicas estándar de Python (`numpy`, `scipy`, `rasterio`, `matplotlib`).
* **Limitaciones de calidad:** Es una suite pedagógica y de referencia metodológica; no es un software de nivel industrial ni un servicio de descarga de datos. Debe adaptarse e integrarse de manera limpia a la arquitectura de AnalogX.
* **Utilidad específica para AnalogX:** Provee las fórmulas matemáticas exactas y algoritmos de referencia en Python para procesar la retrodispersión de microondas y rugosidad en salares terrestres (aplicables tanto a datos de Sentinel-1 como a cualquier fuente SAR en banda C).
* **Prioridad:** **MVP** (como base algorítmica del módulo de rugosidad radar).
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 12: ESA Copernicus Data Space Ecosystem (CDSE)
* **Agencia responsable:** European Space Agency (ESA) y Comisión Europea.
* **Instrumento / Misión / Catálogo:** Flota de satélites Copernicus Sentinel: Sentinel-1 (SAR Banda C en modos IW/EW, polarizaciones VV+VH), Sentinel-2 (Multiespectral MSI VNIR-SWIR en 13 bandas), Sentinel-3 (OLCI color y SLSTR temperatura superficial LST), Sentinel-5P (química atmosférica), y Copernicus DEM (GLO-30 y GLO-90).
* **Variables disponibles:** 
  * *Sentinel-2:* Reflectancia superficial de fondo de atmósfera (*Bottom-Of-Atmosphere - BOA*, Nivel-2A) en 13 bandas espectrales (10 m, 20 m y 60 m), mapa de clasificación de escenas (SCL: nubes, sombras, suelo desnudo, agua/nieve), índices de agua y nieve/sal (NDSI, NDWI).
  * *Sentinel-1:* Coeficiente de retrodispersión $\sigma^0$ calibrado ortorrectificado (GRD) en polarizaciones duales (VV, VH) a 10 m de resolución.
  * *Copernicus DEM:* Elevación digital de superficie global a 30 m sin vacíos de datos.
* **Cobertura geográfica:** Global terrestre sistemática y continua.
* **Resolución espacial:** 10 m (B2, B3, B4, B8 Sentinel-2; S1 GRD), 20 m (B5, B6, B7, B8A, B11, B12 Sentinel-2 para firmas de evaporitas y humedad SWIR), 30 m (Copernicus DEM GLO-30).
* **Cobertura temporal:** 2014 (Sentinel-1) y 2015 (Sentinel-2) hasta el presente. Frecuencia de revisita de 5 días en el Altiplano boliviano.
* **Formatos disponibles:** SAFE format, Cloud-Optimized GeoTIFF (COG), STAC JSON items, y NetCDF.
* **Disponibilidad de API o descarga:** 
  * API OData (`https://zipper.dataspace.copernicus.eu/odata/v1/`).
  * API STAC (`https://stac.dataspace.copernicus.eu/v1/`).
  * Acceso S3 compatible (`eodata.dataspace.copernicus.eu`).
  * OpenEO API.
* **Requisitos de autenticación:** Cuenta gratuita obligatoria en **Copernicus Data Space Ecosystem**. Autenticación moderna vía protocolo OAuth2 / OpenID Connect (Keycloak token endpoint) para generar access tokens Bearer.
* **Licencia:** EU Copernicus Open Access Policy (gratuita, plena y abierta para cualquier propósito científico, educativo o comercial).
* **Tamaño aproximado del producto:** Gránulo individual L2A de Sentinel-2 (baldosa de 100x100 km, ej. cuadrícula MGRS `19KDB` o `19KCB` sobre Uyuni): ~600 MB a 1.1 GB en formato SAFE completo; o descarga individual por bandas en formato COG (B02, B03, B04, B11, B12: ~20-50 MB por banda).
* **Complejidad de procesamiento:** **Media**. El Nivel-2A ya se encuentra corregido atmosféricamente por el procesador Sen2Cor; el cálculo de índices espectrales (NDSI, cocientes SWIR) se realiza mediante operaciones tensoriales vectorizadas en `numpy`/`rasterio`.
* **Limitaciones de calidad:** Época lluviosa en el Altiplano boliviano (diciembre a marzo) genera abundante nubosidad convectiva e inundaciones de la costra salina; requiere filtrado estricto por metadatos de nubosidad (`cloudCover < 10%`) y enmascaramiento con la capa SCL.
* **Utilidad específica para AnalogX:** Fuente de imágenes multiespectrales de alta resolución contemporáneas para mapear la mineralogía evaporítica superficial, variación de albedo y presencia de humedad en el Salar de Uyuni y lagunas salinas de Lípez.
* **Prioridad:** **MVP**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 13: ESA Open Science Catalog
* **Agencia responsable:** European Space Agency (ESA - Earth Observation Open Science).
* **Instrumento / Misión / Catálogo:** Catálogo federado de datasets científicos y productos derivados generados en proyectos de investigación avanzada financiados por la ESA (programas FutureEO, EO Science for Society, Climate Change Initiative - CCI).
* **Variables disponibles:** Datasets temáticos especializados: humedad de suelo superficial a alta resolución, mapas de evaporación y estrés hídrico, modelos geodinámicos, inventarios globales de salinidad de suelos, productos de reflectancia espectral experimental.
* **Cobertura geográfica:** Variable según el proyecto específico (algunos productos son globales, otros cubren transectos regionales o sitios análogos específicos).
* **Resolución espacial:** Muy variable (desde 100 m hasta 25 km según el modelo geofísico).
* **Cobertura temporal:** Heterogénea según la duración de cada consorcio científico (series temporales retrospectivas de 10 a 40 años).
* **Formatos disponibles:** Especificación STAC (SpatioTemporal Asset Catalog), NetCDF-4, GeoTIFF, GeoPackage.
* **Disponibilidad de API o descarga:** STAC API endpoint público (`https://opensciencedata.esa.int/api/stac/v1/`). Enlaces de descarga directos a repositorios abiertos institucionales (Zenodo, CEDA, SEANOE).
* **Requisitos de autenticación:** Depende del dataset específico alojado en el catálogo. La navegación de metadatos STAC es pública; la descarga de algunos paquetes requiere cuenta en ESA SSO o repositorios asociados.
* **Licencia:** Mayoritariamente licencias de ciencia abierta (Creative Commons CC-BY 4.0 o CC0).
* **Tamaño aproximado del producto:** Desde 50 MB hasta decenas de gigabytes por colección de proyecto.
* **Complejidad de procesamiento:** **Media a Alta**. Al tratarse de productos generados por distintos grupos de investigación, la estructura interna de variables en NetCDF puede requerir adaptación individual de metadatos CF (*Climate and Forecast*).
* **Limitaciones de calidad:** No todos los proyectos tienen mantenimiento operativo garantizado a largo plazo ni cobertura garantizada sobre el Altiplano boliviano; los datasets son a menudo demostradores de proyectos (*proof of concept*).
* **Utilidad específica para AnalogX:** Fuente de referencia secundaria para contrastar modelos de balance hídrico y salinidad de suelos validados por la comunidad científica europea.
* **Prioridad:** **Segunda fase**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 14: JAXA G-Portal
* **Agencia responsable:** Japan Aerospace Exploration Agency (JAXA).
* **Instrumento / Misión / Catálogo:** Satélites de observación de la Tierra de JAXA: ALOS / ALOS-2 (radar PALSAR / PALSAR-2 en Banda L), ALOS PRISM (malla de elevación global AW3D30), GCOM-C (sensor óptico multiespectral SGLI), GCOM-W (radiómetro pasivo de microondas AMSR2).
* **Variables disponibles:** 
  * *ALOS-2 PALSAR-2:* SAR en Banda L (longitud de onda $\lambda \approx 23.6\text{ cm}$), polarimetría cuádruple o dual, coeficientes de retrodispersión de microondas.
  * *ALOS AW3D30:* Modelo digital de superficie global a 30 m de resolución derivado de estereoscopía óptica PRISM.
  * *GCOM-C SGLI:* Reflectancia y temperatura de superficie a 250 m.
* **Cobertura geográfica:** Global.
* **Resolución espacial:** PALSAR-2: 1 a 3 m (Spotlight), 6 a 10 m (High Resolution), 100 m (ScanSAR). AW3D30: 1 segundo de arco (~30 m). SGLI: 250 m.
* **Cobertura temporal:** ALOS (2006-2011), ALOS-2 (2014-presente), GCOM-C (2017-presente).
* **Formatos disponibles:** GeoTIFF, CEOS SAR format, HDF5.
* **Disponibilidad de API o descarga:** Protocolo SFTP de descarga directa y descarga web HTTPS a través de la interfaz de G-Portal (`https://www.gportal.jaxa.jp/`). API de catálogo CSW/REST documentada en las guías técnicas de JAXA.
* **Requisitos de autenticación:** Cuenta de usuario registrada obligatoria en **JAXA G-Portal**. El registro es gratuito, pero las solicitudes de datos de radar ALOS-2 de alta resolución en modo experimental requieren justificación de proyecto de investigación o pago de tarifas de datos.
* **Licencia:** JAXA Data Policy (uso científico no comercial para datos estándar de libre distribución como AW3D30; restricciones contractuales para PALSAR-2 de nivel operacional comercial).
* **Tamaño aproximado del producto:** Mosaicos AW3D30: ~30-60 MB por tile de 1°x1°. Escenas PALSAR-2: 1.5 a 4 GB por producto SLC/L2.1.
* **Complejidad de procesamiento:** **Alta**. El procesamiento polarimétrico en banda L requiere herramientas SAR especializadas (SNAP, PolSARpro) y consideración de la constante dieléctrica en medios salinos secos.
* **Limitaciones de calidad:** El proceso de registro y aprobación en G-Portal es más lento y restrictivo que en Earthdata o CDSE; la disponibilidad de escenas gratuitas de ALOS-2 PALSAR-2 sobre Bolivia es limitada en comparación con los archivos públicos de Sentinel-1.
* **Utilidad específica para AnalogX:** La Banda L ($\sim 23.6\text{ cm}$) tiene una profundidad de penetración en costras de sal secas y regolito árido muy superior a la Banda C ($\sim 5.5\text{ cm}$), permitiendo estudiar estructuras subsuperficiales de la halita en Uyuni de forma análoga a cómo el radar SHARAD de la NASA penetra el terreno en Marte.
* **Prioridad:** **Segunda fase**.
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 15: NASA Earth Observatory — Bolivian Salt Flats
* **Agencia responsable:** NASA (Earth Observatory).
* **Instrumento / Misión / Catálogo:** Publicación científica y de teledetección basada en sensores MODIS (satélites Terra y Aqua), OLI (Landsat 8) y altimetría orbital (ICESat GLAS y Envisat RA-2).
* **Variables disponibles:** Análisis de dinámica de reflectancia superficial, rugosidad micrométrica y centimétrica, pendiente extrema (< 1 m de variación vertical a lo largo de 10,000 km²), procesos de inundación estacional, formación de polígonos de desecación de sal, y documentación del uso del Salar de Uyuni como blanco de calibración altimétrica satelital global de la NASA.
* **Cobertura geográfica:** Salar de Uyuni y Salar de Coipasa, Altiplano boliviano (Departamentos de Potosí y Oruro; coordenadas centrales nominales 20.2° S, 67.5° O).
* **Resolución espacial:** N/A (síntesis de investigación de teledetección que sintetiza resoluciones espaciales de 15 m a 250 m).
* **Cobertura temporal:** Registro de observaciones multidecadales (con énfasis en dinámicas 2019-2022 y registros históricos desde la década de 1980).
* **Formatos disponibles:** Artículo científico web estructurado (HTML), imágenes GeoTIFF y JPEG de alta resolución espacial descargables directamente.
* **Disponibilidad de API o descarga:** Acceso web HTTPS directo y libre (`https://science.nasa.gov/earth/earth-observatory/bolivian-salt-flats-151813/`).
* **Requisitos de autenticación:** Ninguno (acceso público abierto).
* **Licencia:** NASA Public Domain (dominio público).
* **Tamaño aproximado del producto:** Páginas web e imágenes asociadas de 2 a 15 MB.
* **Complejidad de procesamiento:** **Baja / Nula**. Actúa como marco bibliográfico oficial y línea base conceptual de calibración.
* **Limitaciones de calidad:** Es una publicación de referencia y síntesis de la NASA, no una base de datos raster interactiva sin procesar.
* **Utilidad específica para AnalogX:** **Sustento de calibración institucional oficial:** Proporciona el respaldo de que la NASA ya reconoce a Uyuni como un entorno hiperplano de calibración de sensores altimétricos y modelo de evaporitas extremas. Se utiliza estrictamente como **sitio de calibración y validación del método**, garantizando que NO se afirme fraudulentamente que Uyuni es un descubrimiento nuevo de este equipo.
* **Prioridad:** **MVP** (referencia metodológica y de calibración).
* **Nivel de verificación:** `Verificado con fuente`.

---

### Recurso 16: NASA Science / JPL / ASU — Chloride Salt Deposit in Southern Highlands of Mars
* **Agencia responsable:** NASA / Jet Propulsion Laboratory (JPL-Caltech) / Arizona State University (ASU Mars Space Flight Facility).
* **Instrumento / Misión / Catálogo:** Mars Odyssey 2001 (Thermal Emission Imaging System - THEMIS) y Mars Reconnaissance Orbiter (High Resolution Imaging Science Experiment - HiRISE).
* **Variables disponibles:** Composición mineralógica por infrarrojo térmico (imágenes decorrelation stretch - DCS utilizando las bandas 8, 7 y 5 de THEMIS a longitudes de onda de 11.04, 11.79 y 12.57 µm, donde los depósitos de cloruro se diferencian en tonos azul brillante / magenta respecto al terreno basáltico circundante amarillento/verdoso); imágenes HiRISE de ultra-alta resolución (`PSP_003160_1410`) que revelan redes de fracturas poligonales de desecación a escala de 1 a 3 metros.
* **Cobertura geográfica:** Cuenca en las tierras altas del sur de Marte, región de **Terra Sirenum**; coordenadas de referencia nominales: **38.8° S de latitud, 221.0° E de longitud** (o 139.0° W en longitud Oeste planetocéntrica).
* **Resolución espacial:** THEMIS Banda Térmica: 100 m/px. HiRISE: ~25 a 50 cm/px.
* **Cobertura temporal:** Adquisición THEMIS ~2007; Adquisición HiRISE `PSP_003160_1410` el 30 de marzo de 2007 (MY 28, Ls = 202.9°).
* **Formatos disponibles:** Ficheros anotados JPEG/TIFF, gránulos de datos científicos EDR/RDR en PDS Imaging Node y ASU THEMIS Data System (`https://themis.asu.edu/`).
* **Disponibilidad de API o descarga:** Acceso público web directo en NASA Science y descarga científica de gránulos en el PDS Geosciences / Imaging Node y ODE REST API (`PSP_003160_1410`).
* **Requisitos de autenticación:** Libre y público, sin autenticación ni registro.
* **Licencia:** NASA / JPL-Caltech Open Access (dominio público).
* **Tamaño aproximado del producto:** 10 MB (imágenes ilustradas) a 250-600 MB (productos HiRISE RDR JP2 / PDS3 completos).
* **Complejidad de procesamiento:** **Media a Alta**. Requiere manipulación de proyecciones cilíndricas equidistantes marcianas, descompresión de ficheros JPEG2000 planetarios de HiRISE y reproyección cartográfica controlada.
* **Limitaciones de calidad:** Los depósitos de cloruro no presentan absorciones diagnósticas en VNIR/SWIR; su detección descansa en la signatura térmica espectral de THEMIS y morfología de cuenca baja; la cobertura HiRISE de detalle se limita a franjas estrechas (~5-6 km de ancho).
* **Utilidad específica para AnalogX:** Define el **objetivo marciano específico del MVP** (`Terra Sirenum 38.8°S, 221.0°E`), estableciendo los parámetros morfométricos y de confinamiento evaporítico contra los cuales se calibra el Salar de Uyuni y se contrastan los candidatos de novedad en el Altiplano boliviano.
* **Prioridad:** **MVP**.
* **Nivel de verificación:** `Verificado con fuente`.

---

## 3. CONCLUSIÓN Y MAPEO PARA LA ARQUITECTURA DE ANALOGX

1. **Fuentes para ingesta y procesamiento activo en el MVP:**
   * Recurso 1 (NASA Earthdata Search / CMR API)
   * Recurso 3 (NASA PDS / ODE REST API)
   * Recurso 6 (NASA AppEEARS REST API)
   * Recurso 7 (NASA MOLA MEG128)
   * Recurso 8 (NASA CRISM MTRDR / literatura)
   * Recurso 11 (CSA SAR Python Tutorial - Algoritmos)
   * Recurso 12 (ESA Copernicus Data Space Ecosystem - Sentinel-2 / COP30)
   * Recursos 15 y 16 (Línea base científica de calibración y objetivo marciano)

2. **Fuentes diferidas a Segunda Fase:**
   * Recursos 4 y 5 (LRO y LRO Diviner para análogos lunares)
   * Recurso 9 (CSA RCM por restricciones de cuota y mayor complejidad frente a Sentinel-1)
   * Recurso 13 (ESA Open Science Catalog)
   * Recurso 14 (JAXA G-Portal ALOS-2 Banda L)

3. **Fuente descartada:**
   * Recurso 10 (RADARSAT-1 histórico; superado técnicamente por Sentinel-1 GRD).

