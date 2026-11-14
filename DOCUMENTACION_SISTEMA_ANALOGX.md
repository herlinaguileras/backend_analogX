# Manual de Arquitectura, Funcionamiento y Flujo Operacional de AnalogX
> **NASA Space Apps Challenge 2026**  
> *Challenge: Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars*  
> **Plataforma:** AnalogX — Planetary Analog Discovery Engine

---

## 1. Resumen Ejecutivo y Problemática de la NASA

### 1.1 El Desafío
Las misiones de exploración espacial tripuladas y robóticas hacia la Luna (**Programa Artemis**) y **Marte** demandan bancos de prueba terrestres ("análogos planetarios") para reducir el riesgo de fallas catastróficas. Sin embargo, la NASA y la comunidad científica rechazan la **similitud visual superficial**: un desierto no es útil para una misión simplemente porque su arena sea roja o su paisaje se parezca a una foto marciana.

### 1.2 Los Tres Pilares Epistemológicos de AnalogX
1. **Contraste de Evidencia Instrumental:** Toda comparación debe sustentarse en variables físicas medidas (reflectancia espectral, pendiente topográfica, capacidad portante y balance termoquímico) contrastadas contra productos satelitales auditados de la NASA, USGS y ESA (MOLA, CRISM, THEMIS, Diviner, LOLA, HiRISE).
2. **Declaración Explícita de Divergencias Físicas ("Dónde falla la analogía"):** Ningún lugar en la Tierra es idéntico al espacio. El sistema declara con honestidad científica las diferencias irreductibles (gravedad terrestre de $1\text{ g}$ vs $0.16\text{ g}$ en la Luna o $0.38\text{ g}$ en Marte; presión atmosférica densa vs vacío absoluto o atmósfera tenue de $6\text{ mbar}$ de $\text{CO}_2$).
3. **Utilidad Operacional de Misión Real:** Cada región debe justificar funcionalmente cómo ayuda a una misión espacial (ensayo de tracción de ruedas para rovers como VIPER, extracción de agua potable mediante procesos ISRU o diseño de hábitats presurizados en tubos de lava para blindaje contra radiación cósmica en Artemis Base Camp).

---

## 2. Arquitectura General del Sistema

El ecosistema de AnalogX está estructurado como una solución desacoplada y modular de alto rendimiento:

```mermaid
flowchart TD
    User([Astrónomo / Evaluador NASA]) <--> UI[Frontend: Next.js 16 + React 19\nPuerto :3100]
    
    subgraph Frontend["Frontend (Next.js 16 / App Router)"]
        ExploreView["/explore: Explorador Satelital + Catálogo"]
        CompareView["/compare: Matriz + Scorecard 7D + Movilidad + ISRU"]
        DossierModal["Dossier Técnico Imprimible (PDF/window.print)"]
        MapLibre["MapLibre GL: Visor Geográfico y Retículas HUD"]
    end
    
    UI --> ExploreView
    UI --> CompareView
    CompareView --> DossierModal
    ExploreView --> MapLibre
    
    UI <-->|Fetch HTTP REST JSON| API[Backend: FastAPI (Uvicorn)\nPuerto :8000]
    
    subgraph Backend["Backend (FastAPI + SQLAlchemy)"]
        Router["app/api/v1/router.py\nEndpoints REST"]
        CatalogData["app/models/catalog_data.py\nMotor de calificación de misiones"]
        DB[(SQLite: analogx.db\nModelos de datos relacionales)]
        Seed["app/core/seed.py\nSeeding automático de datasets NASA"]
    end
    
    API --> Router
    Router --> CatalogData
    Router --> DB
    Seed -.-> DB
```

---

## 3. Módulos y Pantallas del Frontend

### 3.1 Explorador Geográfico (`/explore`)
* **Selector Planetario:** Permite alternar la perspectiva de estudio entre **Marte** (*Terra Sirenum*) y la **Luna** (*Polo Sur Lunar / Artemis*).
* **Filtro de Rol en el Estudio:** Permite segmentar entre *Referencias de calibración* (sitios consolidados con instrumentación previa como el Salar de Uyuni) y *Candidatos de investigación* (nuevas propuestas como las Cuevas Volcánicas de Lípez, Sol de Mañana o Cumbre Licancabur).
* **Visor Cartográfico Interactivo (MapLibre GL):**
  * Capa fotorrealista satelital basada en teselas globales de alta resolución.
  * Capa cartográfica topográfica de contexto geográfico.
  * Pines geográficos con coordenadas precisas (datum WGS84) que al seleccionarse actualizan dinámicamente la vista y la previsualización del terreno.
  * Retículas HUD de estilo centro de control aeroespacial.
* **Ficha de Investigación (Modal):** Despliega el datum científico, la procedencia del localizador, los productos satelitales asociados y la justificación de novedad científica.

---

### 3.2 Matriz Científica y Misiones Espaciales (`/compare`)
Es el núcleo funcional del desafío. Cuenta con cuatro pestañas de trabajo especializadas:

#### Pestaña 1: Matriz de Variables
* Contrasta magnitudes físicas directas entre la Tierra y el objetivo planetario: *Pendiente del terreno*, *Rugosidad superficial*, *Morfología*, *Mineralogía*, etc.
* Enlaces directos hacia las plataformas interactivas de la NASA: **NASA Mars Trek** y **NASA Moon Trek / LROC QuickMap**.

#### Pestaña 2: Scorecard de 7 Dimensiones NASA
Evalúa la rúbrica oficial del Space Apps Challenge mediante 7 tarjetas de telemetría de vuelo:
1. **Geología y Suelo:** Composición mineral (halita, yeso, basaltos) frente a firmas espectrales orbitales.
2. **Terreno y Topografía:** Hiperplanicies poligonales, pendientes y geometría de obstáculos.
3. **Clima Extremo:** Ciclos térmicos extremos, radiación UV a gran altitud y aridez extrema.
4. **Agua y Hielo:** Salmueras hipersalinas eutécticas subsuperficiales y permafrost de alta montaña.
5. **Fenómenos Naturales:** Vientos catabáticos, erosión eólica y actividad hidrotermal fumarólica.
6. **Subsuelo y Refugios:** Tubos de lava, cuevas basálticas y estabilidad estructural.
7. **Biología Extrema:** Extremófilos en salmueras saturadas y biofirmas análogas a depósitos marcianos.

> **Estructura de cada tarjeta:**
> * **Medidor de Fidelidad:** 1 a 5 puntos luminosos.
> * **Alineación Operacional (Match):** Identifica el proceso físico o químico compartido.
> * **Divergencia Física (Límite):** Declara explícitamente dónde falla la analogía (gravedad, atmósfera, vacío).
> * **Protocolo de Prueba Recomendado:** Define el ensayo a ejecutar en campo.
> * **Dataset NASA de Referencia:** Instrumento orbital de calibración (CRISM, MOLA, LOLA, Diviner, HiRISE).

#### Pestaña 3: Movilidad y Tracción de Rovers
* **Análisis Terradinámico:** Capacidad portante del suelo ($\text{kPa}$) y resistencia al punzonamiento.
* **Mapeo de Plataformas Rover:** Asignación automática de plataformas análogas de la NASA (**VIPER Lunar Rover**, **Mars Sample Return Fetch Rover**, **Curiosity**, **Perseverance**).
* **Riesgo de Derrape:** Evaluación con código de alerta (`bajo`, `moderado`, `alto`, `crítico`) con advertencias de hundimiento y desgaste por abrasión en ruedas metálicas de aluminio con tacos *grousers*.
* **Correspondencia de Regolito:** Correlación entre el sustrato terrestre y simulantes de regolito lunar/marciano.

#### Pestaña 4: Hábitat Subterráneo e ISRU (Recursos In-Situ)
* **Extracción ISRU de Agua:** Modelo termoquímico de extracción hídrica a partir de sulfatos hidratados (deshidratación de yeso puro a $150\ ^\circ\text{C}$ con rendimiento de hasta $209\text{ kg H}_2\text{O}/\text{ton}$ y consumo de $0.72\text{ kWh}/\text{kg}$ de agua potable).
* **Aprovechamiento de Subproductos:** Uso de anhidrita ($\text{CaSO}_4$) como material conglomerante para impresión 3D de hábitats permanentes.
* **Blindaje y Hábitat Artemis:** En las Cuevas Volcánicas y Tubos de Lava de Lípez se evalúa:
  * Atenuación de $>95\%$ de Rayos Cósmicos Galácticos (GCR) y Tormentas Solares (SPE) bajo bóvedas de 3 a 6 metros de roca volcánica.
  * Amortiguamiento térmico: exterior de $-25\ ^\circ\text{C}$ a $+18\ ^\circ\text{C}$ frente a un interior constante y estable de $+9.5\ ^\circ\text{C}$.
  * Técnicas de anclaje de módulos habitacionales inflables presurizados.

#### Dossier Técnico NASA (PDF)
* Botón en la esquina superior derecha que abre un modal con el formato de informe técnico formal de misión de la NASA.
* Incluye metadatos geodésicos, puntaje TRL, resumen de las 7 dimensiones, terradinámica y la **Cláusula de Rigor Epistemológico**.
* Un botón **"Imprimir / PDF"** activa la hoja de estilo de impresión optimizada (`window.print()`).

---

### 3.3 Metodología y Bitácora (`/methodology` y `/findings`)
* `/methodology`: Expone la filosofía rectora: *"La evidencia antes que la semejanza"*, detallando las cuatro etapas de trabajo (Contexto geodésico, Procedencia de datos, Compatibilidad de variables y Límites epistemológicos).
* `/findings`: Bitácora científica conectada a la base de datos para registrar hallazgos preliminares y limitaciones reconocidas.

---

## 4. Arquitectura del Backend (FastAPI) y Endpoints REST

El backend está desarrollado con **Python 3.12**, **FastAPI** y **SQLAlchemy**, estructurado bajo patrones de diseño limpios y validación de tipos estricta con **Pydantic v2**:

### 4.1 Catálogo de Endpoints de la API (`/api/v1`)

| Endpoint | Método | Parámetros Query | Descripción |
| :--- | :---: | :--- | :--- |
| `/api/health` | `GET` | — | Verifica conectividad del backend y estado de la base de datos. |
| `/api/regions` | `GET` | `role` (opcional) | Lista las 5 regiones análogas bolivianas con metadatos completos. |
| `/api/regions/{id}` | `GET` | `id` (path) | Detalle científico de una región: geología, citas y datasets satelitales. |
| `/api/compare` | `GET` | `earth_region_id`, `planetary_target_id` | Matriz de variables contrastadas entre Tierra y Marte/Luna. |
| `/api/missions/scorecard` | `GET` | `earth_region_id`, `planetary_target_id` | Genera la evaluación de las **7 dimensiones NASA** con TRL y fidelidad. |
| `/api/missions/mobility` | `GET` | `earth_region_id` | Análisis geotécnico de tracción, derrape y movilidad de rovers. |
| `/api/missions/isru` | `GET` | `earth_region_id` | Modelo termoquímico de extracción de agua potable y balance energético. |
| `/api/missions/habitat-shielding` | `GET` | `earth_region_id` | Amortiguamiento térmico y atenuación de radiación en cavidades subterráneas. |
| `/api/findings` | `GET` | — | Retorna la lista consolidada de hallazgos preliminares. |

### 4.2 Inicialización y Seeding Automático
Al iniciar el servidor FastAPI (`app/main.py`), se ejecuta automáticamente el módulo de seed (`app/core/seed.py`), el cual:
1. Crea las tablas relacionales en la base de datos SQLite local (`analogx.db`).
2. Registra las 7 agencias y fuentes científicas oficiales (NASA PDS, USGS, ESA CDSE, SERGEOMIN).
3. Inserta los 8 productos satelitales oficiales (NASADEM 30m, MOLA MEGDR, HiRISE, CRISM, Diviner, LOLA).
4. Carga las 5 regiones análogas de Bolivia y los 2 objetivos planetarios (Terra Sirenum en Marte y Polo Sur Lunar / Artemis).

---

## 5. Las 5 Regiones Análogas de Bolivia en el Catálogo

1. **Salar de Uyuni (Potosí):**
   * *Rol:* Referencia de calibración.
   * *Analogía:* Hiperplanicie salina evaporítica con costras poligonales de halita ($>95\%\ \text{NaCl}$) idénticas a los paleolagos de *Terra Sirenum* en Marte.
   * *Misión:* Banco de pruebas de odometría visual, altimetría satelital y tracción de rovers (**VIPER / Sample Fetch Rover**).
2. **Sol de Mañana (Reserva Eduardo Avaroa, Potosí):**
   * *Rol:* Candidato de investigación.
   * *Analogía:* Campo geotérmico activo a $>4,850\text{ msnm}$ con fumarolas de azufre, barros hirvientes y ciclos térmicos extremos.
   * *Misión:* Ensayos de biofirmas extremófilas y sensores de corrosión ácida para atmósferas con compuestos sulfurosos.
3. **Tubos de Lava y Cuevas Volcánicas de Lípez (Lípez, Potosí):**
   * *Rol:* Candidato de investigación.
   * *Analogía:* Cavidades volcánicas basálticas-dacíticas estructuralmente competentes, análogas a las fosas de *Marius Hills* y *Mare Tranquillitatis* en la Luna.
   * *Misión:* Prototipado de hábitats presurizados bajo tierra con blindaje radiativo $>95\%$ y estabilidad térmica para **Artemis Base Camp**.
4. **Cumbre Criogénica Licancabur (Potosí - Frontera):**
   * *Rol:* Candidato de investigación.
   * *Analogía:* Lago de cráter de gran altitud ($5,916\text{ msnm}$) expuesto a niveles récord mundiales de radiación UV-B/UV-C y permafrost periglacial.
   * *Misión:* Calibración de espectrómetros Raman y UV para detección de biomoléculas en la superficie marciana.
5. **Altiplano Sur (Potosí / Oruro):**
   * *Rol:* Candidato de investigación.
   * *Analogía:* Cuenca endorreica con paleodepósitos de sulfatos hidratados (yeso dihidratado: $\text{CaSO}_4 \cdot 2\text{H}_2\text{O}$).
   * *Misión:* Ensayos de reactores ISRU para deshidratación mineral y obtención de agua de soporte vital.

---

## 6. Guía de Exposición y Pitch ante los Jueces de la NASA

Si tienes que presentar el proyecto ante los evaluadores del hackathon, enfócate en estos tres mensajes centrales:

> ### 1. "No vendemos paisajes bonitos, contrastamos física real"
> *"Muchos proyectos muestran fotos de desiertos rojos y dicen que se parecen a Marte. AnalogX es un motor científico que contrasta reflectancia espectral de CRISM, modelos digitales de elevación MOLA y capacidad portante del regolito."*

> ### 2. "Aplicamos la regla de oro de la NASA: declarar los límites"
> *"La NASA exige saber dónde falla la analogía. En AnalogX cada evaluación declara la divergencia física insoslayable: la gravedad terrestre ($1\text{ g}$) y la presencia de atmósfera ($1013\text{ hPa}$) frente al vacío lunar y los $0.16\text{ g}$. Le decimos a la agencia espacial qué puede probar aquí y qué debe validar en cámaras de vacío térmico (TVAC)."*

> ### 3. "Utilidad directa para Artemis y Mars Sample Return"
> *"El sistema evalúa las 7 dimensiones de la rúbrica oficial y genera automáticamente protocolos de prueba de tracción de rovers, reactores ISRU para extraer hasta 209 kg de agua por tonelada de yeso, y dimensionamiento de hábitats subterráneos protegidos de la radiación cósmica."*

---

## 7. Instrucciones para Ejecutar el Proyecto Localmente

### Backend (FastAPI en Python)
```bash
cd ~/Desktop/backend_analogX
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
* **Swagger UI interactivo:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Verificación de endpoints:** [http://localhost:8000/api/missions/scorecard?earth_region_id=salar-de-uyuni&planetary_target_id=terra-sirenum](http://localhost:8000/api/missions/scorecard?earth_region_id=salar-de-uyuni&planetary_target_id=terra-sirenum)

### Frontend (Next.js 16)
```bash
cd ~/Desktop/frontend_analogX
npm start -- -p 3100
```
* **Explorador Satelital:** [http://localhost:3100/explore](http://localhost:3100/explore)
* **Comparador de Misiones:** [http://localhost:3100/compare?region=salar-de-uyuni&body=Mars](http://localhost:3100/compare?region=salar-de-uyuni&body=Mars)
* **Ejecutar Pruebas de Humo:**
  ```bash
  npm run test:smoke
  ```
