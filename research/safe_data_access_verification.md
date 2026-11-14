# PROTOCOLO DE VERIFICACIÓN SEGURA DE ACCESOS Y DISPONIBILIDAD
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `research/safe_data_access_verification.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Estatus:** Protocolo de verificación seguro  

---

## 1. PRINCIPIOS DE VERIFICACIÓN SEGURA (SIN CREDENCIALES NI DESCARGAS MASIVAS)

Para cumplir con las restricciones del proyecto y no saturar redes ni violar condiciones de servicio:
1. **Verificación de Metadatos primero:**  
   Se consultan exclusivamente endpoints de catálogo (`search`, `status`, `health`, `metadata`, `STAC items`, `CMR granules`) usando peticiones `HEAD` o `GET` filtradas con límite `limit=1`.
2. **Descarga Cero en Fase 0:**  
   No se ejecutan descargas de imágenes completas ni gránulos masivos de gigabytes.
3. **No simulación de éxito:**  
   Si un endpoint requiere autenticación (ej. Earthdata Login o Copernicus Keycloak), se documenta explícitamente el estado `Requiere autenticación previa (401/403)` en lugar de simular que la descarga fue exitosa sin credenciales.

---

## 2. PROCEDIMIENTO PASO A PASO PARA EL EQUIPO

### Paso 1: Verificación de NASA CMR Search API (Público sin credenciales para búsqueda)
```bash
# Consulta pública de disponibilidad del dataset NASADEM_HGT sobre el Salar de Uyuni
curl -s "https://cmr.earthdata.nasa.gov/search/granules.json?short_name=NASADEM_HGT&version=001&point=-67.5,-20.2&page_size=1" | jq .
```
* **Respuesta esperada:** JSON con `feed.entry` conteniendo metadatos del gránulo `NASADEM_HGT_s21w068.hgt`, enlaces HTTPS al LP DAAC y tamaño del archivo (~15-25 MB).
* **Autenticación requerida para búsqueda:** Ninguna.
* **Autenticación requerida para descarga del archivo `.hgt`:** Sí, NASA Earthdata Login URS.

---

### Paso 2: Verificación de NASA PDS Geosciences Orbital Data Explorer (ODE) REST API
```bash
# Consulta de observaciones HiRISE y CRISM sobre Terra Sirenum (-38.8 Lat, 221.0 Lon Este)
curl -s "https://oderest.rsl.wustl.edu/live2/?target=mars&query=product&pt=PSP_003160_1410&output=JSON" | jq .
```
* **Respuesta esperada:** JSON con metadatos del producto HiRISE `PSP_003160_1410`, fecha de adquisición `2007-03-30`, centroides y enlaces de descarga PDS.
* **Autenticación requerida:** Ninguna. Acceso público abierto y gratuito.

---

### Paso 3: Verificación de WUSTL PDS Geosciences MOLA Server
```bash
# Comprobación de cabecera HTTP del archivo de cuadrícula MOLA MEG128
curl -I -s "https://pds-geosciences.wustl.edu/mgs/mgs-m-mola-5-megdr-l3-v1/mgsl_300x/meg128/megt90n000cb.lbl"
```
* **Respuesta esperada:** Código HTTP `200 OK` con tipo de contenido `text/plain` correspondiente a la cabecera PDS3.
* **Autenticación requerida:** Ninguna.

---

### Paso 4: Verificación de ESA Copernicus Data Space Ecosystem (CDSE) STAC API
```bash
# Consulta de catálogo de escenas Sentinel-2 L2A sobre el Salar de Uyuni
curl -s "https://stac.dataspace.copernicus.eu/v1/collections/SENTINEL-2/items?bbox=-68.0,-20.5,-67.0,-20.0&limit=1" | jq .
```
* **Respuesta esperada:** GeoJSON FeatureCollection con metadatos de la escena, identificador `S2A_MSIL2A_...` o `S2B_MSIL2A_...`, cobertura de nubes y enlaces de descarga de assets.
* **Autenticación requerida para búsqueda STAC:** Pública.
* **Autenticación requerida para descargar bandas individuales:** Sí, token OAuth2 Bearer de Copernicus CDSE.

---

### Paso 5: Verificación de Repositorio CSA SAR Tutorial
```bash
# Comprobación de existencia del repositorio de tutoriales SAR en GitHub
curl -I -s "https://api.github.com/repos/asc-csa/Synthetic_Aperture_Radar_Tutorial"
```
* **Respuesta esperada:** Código HTTP `200 OK` con información del repositorio público.
* **Autenticación requerida:** Ninguna.

---

## 3. RESUMEN DE PERMISOS, CREDENCIALES Y DEPENDENCIAS REQUERIDAS

| Proveedor / Servicio | Tipo de Acceso a Metadatos | Tipo de Acceso a Datos Crudos | Credencial Necesaria | Costo |
|---|---|---|---|---|
| **NASA Earthdata (CMR / AppEEARS)** | Público abierto | Restringido a usuarios registrados | NASA Earthdata Login (URS) | Gratuito |
| **NASA PDS (Geosciences / ODE)** | Público abierto | Público abierto | Ninguna | Gratuito |
| **ESA Copernicus Data Space (CDSE)** | Público abierto (STAC) | Restringido a usuarios registrados | Cuenta CDSE + Token OAuth2 | Gratuito |
| **Canadian Space Agency (EODMS)** | Restringido | Restringido (aprobación) | Cuenta EODMS del Gob. de Canadá | Gratuito (Sujeto a cuota) |
| **JAXA G-Portal** | Público abierto | Restringido a usuarios registrados | Cuenta registrada G-Portal | Gratuito (Datos estándar) |
| **GitHub (CSA SAR Tutorial)** | Público abierto | Público abierto | Ninguna | Gratuito |

