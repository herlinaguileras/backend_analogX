# INVESTIGACIÓN DE CANDIDATOS DE ANALOGÍA PLANETARIA EN BOLIVIA
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `research/bolivia_candidates.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Región de estudio:** Altiplano Sur y Cordillera Occidental de los Andes (Departamentos de Potosí y Oruro, Bolivia)  
> **Estatus:** Aprobado para catálogo geoespacial  

---

## 1. INTRODUCCIÓN Y ESTRATEGIA DE SELECCIÓN

Para cumplir con el rigor científico exigido por NASA Space Apps Challenge 2026, la selección de sitios análogos terrestres en Bolivia se estructura en dos categorías operativas diferenciadas:

1. **Sitio de Referencia y Calibración Metodológica (Salar de Uyuni):**  
   NASA y la comunidad geológica internacional ya reconocen a Uyuni y Coipasa como ambientes evaporíticos y de calibración altimétrica de primer nivel (*NASA Earth Observatory, 2022; Borsa et al., 2008*). **No se declara como un descubrimiento nuevo**, sino como el patrón de referencia terrestre con datos hiper-verificados para calibrar el algoritmo, las transformaciones de coordenadas y la detección de polígonos de desecación.
2. **Candidatos de Investigación y Novedad Científica (Sol de Mañana y Cuencas de Lípez):**  
   Regiones menos caracterizadas en bases de datos integradas de análogos espaciales, donde la interacción entre vulcanismo activo/relicto, fluidos hidrotermales de alta cota (~4,850 msnm), salmueras ácidas/alcalinas y extrema radiación UV aporta un modelo análogo complementario para el Marte temprano (Noachiano tardío / Hesperiano).

---

## 2. SITIO DE REFERENCIA DE CALIBRACIÓN: SALAR DE UYUNI

### 2.1 Ficha General
* **Nombre oficial:** Salar de Uyuni (Gran Salar de Tunupa).
* **Ubicación política:** Departamentos de Potosí (Provincia Daniel Campos) y Oruro (Provincia Ladislao Cabrera), Bolivia.
* **Bounding Box (WGS84 / EPSG:4326):**
  * Latitud: $[-20.80^\circ\text{ S}, -19.80^\circ\text{ S}]$
  * Longitud: $[-68.10^\circ\text{ O}, -67.10^\circ\text{ O}]$
  * Coordenadas centrales nominales: **$20.25^\circ\text{ S}, 67.60^\circ\text{ O}$**
* **Altitud media:** ~3656 msnm (referencia EGM96).
* **Extensión superficial:** ~10,582 km² (la mayor costra continua de evaporitas del planeta).
* **Rol en AnalogX:** **Patrón de calibración metodológica**.

```
                  ┌─────────────────────────────────────────┐ -19.80° S
                  │              SALAR DE UYUNI             │
                  │                                         │
                  │        [Sector Central - Halita Pura]   │
                  │                 (Isla Incahuasi)        │
                  │                                         │
                  │   [Delta Río Grande]                    │
                  │                                         │
                  └─────────────────────────────────────────┘ -20.80° S
                 -68.10° O                                 -67.10° O
```

### 2.2 Sectores Específicos Analizados en Uyuni

#### Sector A: Núcleo Central de Halita Masiva
* **Características:** Costra de cloruro de sodio ($NaCl$) de pureza superior al 95-99%, con espesores que varían entre 2 y más de 10 metros, intercalada con finas capas de sedimentos clásticos y salmueras intersticiales ricas en $Li, Mg, K, B$.
* **Morfometría:** Pendiente regional horizontal casi nula ($< 0.05^\circ$, variación vertical $< 0.8\text{ m}$ a lo largo de 50 km).
* **Análogo con Marte:** Modelo de sedimentación en el centro de paleolagos evaporíticos terminales donde el secado completo de la salmuera depositó cloruros sin aporte clástico proximal.

#### Sector B: Delta del Río Grande de Lípez
* **Ubicación:** Borde sur-sureste del salar (~$20.75^\circ\text{ S}, 67.25^\circ\text{ O}$).
* **Características:** Zona de transición hidrológica donde un curso fluvial activo desemboca en la cuenca evaporítica salina, transportando arcillas, arenas volcánicas y solutos disueltos.
* **Análogo con Marte:** Representa un análogo de los canales y abanicos aluviales que desembocan en depresiones con cloruros en Marte (ej. canales invertidos y valles que alimentan cuencas en Terra Sirenum documentados por Osterloo et al., 2010 e Hynek et al., 2015).

#### Sector C: Borde Occidental y Paleo-costas (Isla Incahuasi)
* **Ubicación:** $20.245^\circ\text{ S}, 67.625^\circ\text{ O}$.
* **Características:** Elevación volcánica residual en medio del salar con presencia de terrazas lacustres fósiles, costras de calcáreo y arrecifes fósiles de estromatolitos depositados por los paleolagos precursores (Lago Minchin y Lago Tauca, 40,000 a 12,000 años antes del presente).
* **Análogo con Marte:** Modelo de biofirmas fósiles en paleolíneas de costa de cuencas lacustres marcianas cerradas, donde la preservación de estructuras biogénicas o carbonáticas ocurre en los márgenes rocosos protegidos de la disolución.

#### Sector D: Redes Poligonales de Desecación
* **Características:** Retículas poligonales de halita de **1 a 3 metros de diámetro** formadas por contracción térmica y desecación activa, con rebordes sobreelevados de sal de 5 a 15 cm.
* **Análogo con Marte:** Calibrador dimensional directo frente a los polígonos de desecación de 1 a 5 metros de diámetro observados en el depósito de cloruro de Terra Sirenum por la cámara HiRISE de la NASA (`PSP_003160_1410`).

---

## 3. CANDIDATO DE INVESTIGACIÓN (NOVEDAD): CAMPO GEOTERMAL SOL DE MAÑANA

### 3.1 Ficha General
* **Nombre oficial:** Campo Geotermal Sol de Mañana.
* **Ubicación política:** Departamento de Potosí, Provincia Sur Lípez, Reserva Nacional de Fauna Andina Eduardo Abaroa, Bolivia.
* **Bounding Box (WGS84 / EPSG:4326):**
  * Latitud: $[-22.08^\circ\text{ S}, -22.01^\circ\text{ S}]$
  * Longitud: $[-67.79^\circ\text{ O}, -67.72^\circ\text{ O}]$
  * Coordenadas centrales nominales: **$22.05^\circ\text{ S}, 67.76^\circ\text{ O}$**
* **Altitud media:** ~4,850 a 5,000 msnm.
* **Extensión del área activa:** ~10 a 15 km².
* **Rol en AnalogX:** **Candidato de novedad científica**.

```
       Sol de Mañana (~4,850 msnm)
       ┌───────────────────────────────┐ -22.01° S
       │   Fumarolas de Alta Enthalpía │
       │   Ollas de Lodo Hirviente     │
       │   Depósitos de Azufre Nativo  │
       │   Alteración Sílice-Sulfato   │
       └───────────────────────────────┘ -22.08° S
      -67.79° O                       -67.72° O
```

### 3.2 Características Científicas Relevantes
1. **Actividad Hidrotermal de Alta Cota:**
   Campo geotermal volcánico activo de alta entalpía ubicado en una caldera dacítica/riolítica. Se caracteriza por fumarolas de vapor sobrecalentado ($T \approx 85 - 92^\circ\text{C}$, temperatura de ebullición del agua a ~4,850 msnm), geiseres, pozas de lodo ácido hirviente (*mud pots*) y manantiales sulfurosos.
2. **Asociación Mineralógica Excepcional:**
   * Depósitos de azufre nativo elemental ($S_8$) en bocas de fumarola.
   * Alteración hidrotermal ácida avanzada (sulfatación de rocas volcánicas produciendo alunita, caolinita y yeso).
   * Eflorescencias de sales hidrotermales y precipitados de sílice amorfa opalina ($SiO_2 \cdot nH_2O$).
3. **Factores Ambientales Extremos:**
   * Presión atmosférica reducida: ~540 mbar (~54 kPa).
   * Radiación UV extrema con índice UV de pico > 25.
   * Amplitud térmica diurna-nocturna extrema (noches invernales de hasta $-25^\circ\text{C}$).
   * Hiperaridez atmosférica con vientos de alta velocidad constantes.

### 3.3 Tipo de Analogía Planetaria Propuesta
* **Análogo de Sistemas Hidrotermales del Marte Temprano:**  
  Durante el Noachiano tardío y Hesperiano, el decaimiento del vulcanismo marciano y el enfriamiento planetario propiciaron la interacción de magmas residuales con aguas subterráneas, generando sistemas hidrotermales hidrovolcánicos.
  * **Análogo con Home Plate (Cráter Gusev):** Los depósitos de sílice pura descubiertos por el rover Spirit en Home Plate han sido interpretados por la NASA como depósitos de fumarolas o manantiales hidrotermales calientes (*Squyres et al., 2008*). Sol de Mañana ofrece un laboratorio natural activo a baja presión atmosférica para estudiar la precipitación de sílice y sulfatos en condiciones de alta radiación.
  * **Conexión con Terra Sirenum / Cuenca de Eridania:** Investigaciones recientes (*Michalski et al., 2017, Nature Communications*) indican que los cloruros y filosilicatos de Terra Sirenum y el paleolago Eridania estuvieron asociados a actividad hidrotermal sublacustre y manantiales hidrotermales profundos. Sol de Mañana modela el régimen de interacción fluido-roca previo al secado evaporítico terminal.

### 3.4 Nivel de Novedad Científica frente a Estudios Previos
* **Justificación bibliográfica:** Mientras que el Salar de Uyuni cuenta con más de 200 publicaciones sobre calibración de satélites y geoquímica básica, Sol de Mañana **rara vez ha sido integrado en plataformas de datos geoespaciales planetarias abiertas de forma cuantitativa** como análogo específico de desgasificación volcánica y alteración por sulfato-sílice en relación a Terra Sirenum. Su modelado aporta originalidad científica neta al proyecto.

### 3.5 Limitaciones Físicas y Ambientales
* **Vulcanismo activo vs extinto:** Sol de Mañana es un sistema magmático activo con aporte de calor moderno; Marte ya no presenta actividad hidrotermal activa superficial detectable.
* **Atmósfera oxidante:** Los fluidos hidrotermales en Bolivia interactúan con una atmósfera terrestre con 21% de $O_2$, lo que oxida rápidamente el azufre a sulfatos ($SO_4^{2-}$); en el Marte primitivo la atmósfera era dominada por $CO_2$, lo que favorecía fases de azufre reducido o estados de valencia intermedios.

### 3.6 Datos Necesarios para su Validación en Fase 1
* **Topografía:** NASADEM_HGT para derivar pendientes de la caldera volcánica y zonas de descarga.
* **Multiespectral:** Bandas SWIR de Sentinel-2 (B11 a 1.61 µm y B12 a 2.19 µm) y ratios espectrales de alteración hidrotermal (Alunita/Caolinita = B12/B11; Silicatos = B11/B04).
* **Térmico:** Landsat 8/9 TIRS (Bandas 10 y 11) o ASTER GED para delimitar las anomalías de flujo térmico superficial de las fumarolas.

---

## 4. CANDIDATOS ADICIONALES DEL ALTIPLANO SUR / LÍPEZ

### 4.1 Laguna Pastos Grandes
* **Ubicación:** $21.63^\circ\text{ S}, 67.82^\circ\text{ O}$, altitud ~4,400 msnm.
* **Contexto geológico:** Caldera volcánica colapsada anidada que alberga una laguna salina poco profunda y extensos domos y mantos de travertino ($CaCO_3$) activos y fósiles.
* **Relevancia análoga:** Modelo de sedimentación carbonatada y evaporitas ricas en litio y boro asociadas al colapso de calderas volcánicas, análogo a calderas marcianas que contuvieron fluidos alcalinos efímeros (ej. caldera de Apolinaris Patera o depresiones tectónicas de Nili Fossae).

### 4.2 Laguna Colorada
* **Ubicación:** $22.20^\circ\text{ S}, 67.77^\circ\text{ O}$, altitud ~4,278 msnm.
* **Contexto geológico:** Laguna salina somera endorreica con salmueras ricas en sulfatos de sodio y magnesio, bórax y sedimentos diatomáceos.
* **Relevancia análoga:** Pigmentación rojiza provocada por sedimentos minerales y extremófilos halófilos (*Dunaliella salina*) bajo niveles extremos de radiación UV; análogo de biofirmas bajo estrés solar severo.

### 4.3 Sistema Laguna Verde / Laguna Blanca (Pie del Volcán Licancabur)
* **Ubicación:** $22.80^\circ\text{ S}, 67.80^\circ\text{ O}$, altitud ~4,350 msnm.
* **Contexto geológico:** Cuencas lacustres hipersalinas de alta montaña dominadas por sulfato de magnesio y arsénico, ubicadas en el límite con Chile al pie del estratovolcán Licancabur.
* **Relevancia análoga:** Estudiado pioneramente por expediciones de Nathalie Cabrol (NASA Ames / SETI Institute) como el análogo terrestre más cercano a las condiciones de lagos del Marte temprano bajo atmósfera enrarecida y alta radiación UV.

---

## 5. TABLA COMPARATIVA DE SITIOS BOLIVIANOS PARA ANALOGX

| Sitio | Coordenadas Nominales | Cota Media | Proceso Análogo Principal | Fase Análoga Marciana | Rol en AnalogX | Novedad Bibliográfica |
|---|---|---|---|---|---|---|
| **Salar de Uyuni** | $20.25^\circ\text{ S}, 67.60^\circ\text{ O}$ | 3,656 msnm | Desecación evaporítica masiva, halita pura, polígonos métricos | Noachiano tardío / Hesperiano (Lagos terminales) | **Sitio de Calibración** | Baja (Muy documentado por NASA) |
| **Sol de Mañana** | $22.05^\circ\text{ S}, 67.76^\circ\text{ O}$ | 4,850 msnm | Fumarolas geotermales, alteración sílice-sulfato, desgasificación | Noachiano temprano-medio (Hidrotermalismo / Home Plate) | **Candidato de Novedad** | **Alta** (Novedoso en catálogos de SIG planetario) |
| **Laguna Pastos Grandes** | $21.63^\circ\text{ S}, 67.82^\circ\text{ O}$ | 4,400 msnm | Travertinos carbonatados y salmueras en caldera colapsada | Noachiano tardío (Calderas con lagos efímeros) | Candidato Secundario | Media-Alta |
| **Laguna Colorada** | $22.20^\circ\text{ S}, 67.77^\circ\text{ O}$ | 4,278 msnm | Evaporitas de sulfato-boro y biofirmas bajo UV extrema | Hesperiano (Cuencas salinas ácidas/neutras) | Candidato Secundario | Media |
| **Laguna Verde / Blanca** | $22.80^\circ\text{ S}, 67.80^\circ\text{ O}$ | 4,350 msnm | Lagos hipersalinos volcánicos al pie de estratovolcanes | Transición Noachiano-Hesperiano (Paleolagos de impacto/volcánicos) | Validación Externa | Media (Estudios SETI previos) |

