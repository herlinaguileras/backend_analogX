# AnalogX — Planetary Analog Discovery Engine (Backend)

[![NASA Space Apps Challenge 2026](https://img.shields.io/badge/NASA%20Space%20Apps-2026-blue.svg)](https://spaceappschallenge.org/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.16+-00b0ff.svg)](https://sqlmodel.tiangolo.com/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2.6+-e92063.svg)](https://docs.pydantic.dev/)

Repositorio oficial del **Backend** de **AnalogX — Planetary Analog Discovery Engine**, desarrollado para el **NASA Space Apps Challenge 2026: *Permanent Moon Base Locations and Mars***.

AnalogX es un motor analítico y geoespacial diseñado para identificar, caracterizar y comparar de forma verificable regiones terrestres de Bolivia que comparten procesos geológicos, físicos, subterráneos y térmicos relevantes con paleocuencas de **Marte** y sitios candidatos para la **Base Lunar Permanente del Programa Artemis**, respaldado exclusivamente por datos abiertos de agencias espaciales (NASA, ESA, USGS).

---

## 1. Guía Rápida de Instalación y Ejecución

Sigue estos pasos para clonar, instalar dependencias, inicializar la base de datos y correr el servidor:

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/herlinaguileras/backend_analogX.git
cd backend_analogX
```

### Paso 2: Crear y activar el entorno virtual
```bash
# En Linux / macOS / WSL:
python3 -m venv venv
source venv/bin/activate

# En Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Paso 3: Instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 4: Poblar la Base de Datos (Seed)
Ejecuta el script de inicialización para crear la base de datos SQLite (`analogx.db`) con todos los datos científicos oficiales:
```bash
python scripts/seed_database.py
```
> **Nota:** La base de datos es idempotente; puedes ejecutar este comando tantas veces como desees sin duplicar registros. Además, al iniciar el servidor FastAPI, el ciclo de vida de la aplicación (`lifespan`) inicializa y verifica automáticamente la base de datos.

### Paso 5: Iniciar el Servidor de Desarrollo
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Paso 6: Verificar en el Navegador
* **Documentación interactiva Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Documentación ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)
* **Metadatos e hipótesis:** [http://localhost:8000/api/info](http://localhost:8000/api/info)

---

## 2. Contenido de la Base de Datos (`analogx.db`)

El script de *seed* puebla las entidades científicas clave estructuradas para el reto:

### A. Regiones Análogas Terrestres en Bolivia (5 regiones)
1. **Salar de Uyuni:** Sitio patrón hiperplano de calibración altimétrica global de satélites (ICESat / LOLA) y ensayos de tracción de rovers.
2. **Sol de Mañana (Sur Lípez):** Campo geotermal activo (~4850 msnm) con fumarolas, lodos hirvientes y sílice opalina, análogo del vulcanismo hidrotermal del Marte temprano (Home Plate / Cráter Gusev).
3. **Tubos de Lava y Cuevas de Lípez:** Cavidades volcánicas subterráneas a gran altitud para ensayar **hábitats presurizados y blindaje antirradiación de la Base Lunar Permanente Artemis**.
4. **Cumbre Criogénica Licancabur:** Volcán periglacial a ~5916 msnm con frío nocturno de hasta -25 °C y radiación UV biocida para pruebas térmicas de trajes espaciales EVA (xEMU).
5. **Altiplano Sur:** Corredor regional para evaluar gradientes de salinidad y desecación.

### B. Objetivos Planetarios Extraterrestres (2 objetivos)
1. **Terra Sirenum (Marte):** Depósitos de sales de cloruro en paleocuencas cerradas del Noachiano-Hesperiano (~38.8°S, 221.0°E).
2. **Polo Sur Lunar (Cráter Shackleton / Macizo Malapert):** Región de alunizaje y candidata principal para la Base Lunar Artemis, combinando picos de luz casi continua (>85%) y regiones en sombra permanente (PSR a 40 K) con hielo de agua.

### C. Casos de Uso para Misiones Espaciales Reales
1. `use_rover_mobility_uyuni`: Ensayos de tracción, deslizamiento y fatiga de ruedas metálicas en costras de halita para rovers marcianos y lunares (VIPER / MSR).
2. `use_instrument_sherloc_sol_de_manana`: Calibración y validación de espectrómetros Raman y XRF (SHERLOC / SuperCam de Perseverance).
3. `use_lunar_base_shelter_lipez`: Acondicionamiento de refugios subterráneos y blindaje antirradiación para la Base Lunar Artemis.
4. `use_isru_water_extraction_uyuni`: Extracción térmica de agua desde minerales evaporíticos hidratados (ISRU).
5. `use_eva_thermal_licancabur`: Ensayos de fatiga térmica y vacío parcial para trajes espaciales Artemis xEMU.

### D. Datasets Científicos Oficiales Integrados
* **NASA MOLA MEGDR** (MGS, 463 m/px)
* **NASA THEMIS IR DCS** (Mars Odyssey, 100 m/px)
* **NASA HiRISE** (MRO, 0.25 m/px)
* **NASA LRO LOLA DEM** (Lunar Reconnaissance Orbiter, 20 m/px polar)
* **NASA LRO Diviner LST** (Temperaturas superficiales y estabilidad de hielo lunar)
* **NASA SRTM / NASADEM** (30 m global)
* **ESA Copernicus DEM** (30 m TanDEM-X)
* **ESA Sentinel-2 MSI L2A** (10-20 m reflectancia BOA)

---

## 3. Endpoints Principales de la API

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/health` | Diagnóstico de disponibilidad del servidor |
| `GET` | `/api/info` | Hipótesis científica, metadatos y reglas epistemológicas |
| `GET` | `/api/regions` | Catálogo de regiones terrestres bolivianas |
| `GET` | `/api/regions/{id}` | Ficha científica con datasets, citas y casos de uso asociados |
| `GET` | `/api/targets` | Objetivos planetarios (Marte y Luna Artemis) |
| `POST` | `/api/compare` | Comparación física estructurada variable por variable |
| `GET` | `/api/missions/use-cases` | Casos de uso clasificados por misión y categoría |
| `GET` | `/api/sources` | Organismos oficiales (NASA PDS, Moon Trek, Mars Trek, CDSE) |
| `GET` | `/api/findings` | Bitácora de hallazgos científicos validados |

---

## 4. Estructura del Repositorio

```
backend_analogX/
├── app/
│   ├── main.py                     # Entrypoint FastAPI, CORS y lifespan
│   ├── core/
│   │   ├── config.py               # Configuración centralizada
│   │   ├── database.py             # Motor SQLite, sesiones y ruta absoluta
│   │   └── seed.py                 # Lógica de población científica oficial
│   ├── models/                     # Esquemas Pydantic y modelos SQLModel
│   │   ├── db_models.py            # Modelos de persistencia relacional
│   │   ├── frontend.py             # Contratos de transporte y misiones
│   │   ├── catalog_data.py         # Repositorio en memoria y comparador
│   │   ├── dataset.py              # Esquemas de datasets
│   │   ├── region.py               # Esquemas de regiones
│   │   └── evidence.py             # Evidencias y limitaciones físicas
│   └── api/
│       └── v1/
│           └── router.py           # Endpoints de la API REST
├── research/                       # Documentación científica y auditorías
├── scripts/
│   ├── __init__.py
│   └── seed_database.py            # CLI runner para poblar la BD
├── tests/
│   └── test_models.py              # Suite de pruebas unitarias
├── requirements.txt                # Dependencias Python
├── pyproject.toml                  # Configuración del proyecto
└── README.md                       # Documentación del proyecto
```

---

## 5. Pruebas Unitarias

Para verificar que todos los modelos y validaciones funcionen correctamente:
```bash
python tests/test_models.py
```

---

## 6. Licencia y Créditos

Desarrollado bajo principios de **Ciencia Abierta (*Open Science*)** para el **NASA Space Apps Challenge 2026**.  
Todos los datos orbitales y planetarios provienen de los archivos públicos de **NASA Planetary Data System (PDS)**, **NASA Solar System Treks**, **LROC**, **ESA Copernicus** y **USGS EROS**.
