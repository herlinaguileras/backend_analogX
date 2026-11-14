# EVALUACIÓN DE COMPARABILIDAD CIENTÍFICA TIERRA-MARTE
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `research/earth_mars_comparability.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Área temática:** Geología planetaria, geomorfología cuantitativa y teledetección comparada  
> **Estatus:** Aprobado para modelado de datos  

---

## 1. MARCO EPISTEMOLÓGICO Y REGLAS CIENTÍFICAS ESTRICTAS

La analogía planetaria es una herramienta heurística de inferencia geológica, **NO una afirmación de equivalencia ambiental total ni una certificación de idoneidad para la habitabilidad o asentamiento humano**. En el contexto de AnalogX, la comparación entre el Altiplano boliviano (Salar de Uyuni y cuencas volcánico-evaporíticas de Lípez) y las tierras altas del sur de Marte (depósitos de cloruro en Terra Sirenum) se somete a tres **reglas metodológicas inviolables**:

> [!CAUTION]
> **REGLA 1: Prohibición de comparar elevaciones absolutas entre datums planetarios incompatibles.**
> Las elevaciones terrestres (ej. ~3656 msnm en el Salar de Uyuni o ~4850 msnm en Sol de Mañana) están referenciadas al geoide gravitacional terrestre (EGM96) o elipsoide WGS84, vinculado a la hidrosfera activa y nivel del mar. En Marte, las elevaciones de MOLA se miden respecto al Areoide marciano (superficie equipotencial gravitacional con radio ecuatorial medio de 3396.0 km), el cual no tiene relación física ni hidrológica con el nivel medio del mar terrestre.
> *Operación científica válida:* **Únicamente se comparan métricas relativas y derivadas intrínsecas a la cuenca:** desniveles locales ($\Delta z = z_{\text{borde}} - z_{\text{fondo}}$), pendientes de contorno ($\nabla z$), gradientes topográficos adimencionales y curvatura espacial.

> [!WARNING]
> **REGLA 2: Prohibición de convertir observaciones visuales o de albedo en afirmaciones mineralógicas.**
> Un área con alto albedo o tonalidad clara en imágenes ópticas visibles (ej. HiRISE o Sentinel-2) puede deberse a acumulación de halita, sulfatos hidratados, polvo fino eólico basáltico deshidratado, escarcha de $CO_2/H_2O$ transitoria o simple dispersión especular. 
> *Operación científica válida:* La presencia de cloruros o especies minerales sólo se afirma cuando está respaldada por espectroscopía diagnóstica en el infrarrojo térmico (THEMIS bandas DCS 8-7-5), absorciones infrarrojas (CRISM SWIR) o análisis geoquímicos in situ/muestreo de laboratorio contrastado. El dato visual se cataloga estrictamente como *textura/morfología*.

> [!IMPORTANT]
> **REGLA 3: Prohibición de confundir paleoprocesos marcianos con condiciones ambientales contemporáneas terrestres.**
> Los depósitos de cloruro de Terra Sirenum se formaron durante la transición Noachiano tardío a Hesperiano temprano (hace entre 3.8 y 3.5 mil millones de años), bajo una atmósfera marciana más densa que permitía la estabilidad transitoria de agua líquida o surgencia freática en cuencas cerradas. Las condiciones superficiales actuales de Marte (presión ~6 mbar, hiperaridez sin agua líquida superficial, frío radiativo extremo) no deben confundirse con la época formadora de los depósitos ni con la dinámica activa de inundación-evaporación anual que ocurre hoy en Uyuni.

---

## 2. MATRIZ DE COMPARABILIDAD VARIABLE POR VARIABLE

| Variable / Dimensión | Tipo de Comparación | Unidades Terrestres vs Marcianas | Compatibilidad de Resolución | Necesidad de Remuestreo | Incertidumbres Principales | Diferencias Físicas No Reducibles |
|---|---|---|---|---|---|---|
| **1. Pendiente ($\nabla z$)** | **Directa** (adimensional o angular) | Grados (°) o % (m/m) en ambos cuerpos | Terrestre: 30 m (NASADEM). Marte: 463 m (MOLA MEG128) o ~1-2 m (HiRISE DEM) | **Sí**, remuestreo espacial o filtrado por longitud de onda espacial | Suavizado subpíxel en MOLA por espaciamiento orbital; sesgo en escarpes abruptos | Gravedad diferencial ($g_{T}=9.81\text{ m/s}^2$ vs $g_{M}=3.71\text{ m/s}^2$) condiciona el ángulo de reposo de taludes clásticos |
| **2. Rugosidad Superficial** | **Indirecta** (estadística) | Desviación estándar de alturas RMS ($m$), exponente de Hurst ($H$), coeficiente de retrodispersión radar $\sigma^0$ (dB) | Terrestre: 10 m (S1 SAR), 30 m (DEM). Marte: 463 m (MOLA) y perfiles PEDR (300 m) | **Sí**, estandarización a la misma línea de base métrica ($L_0$) | Efecto de la longitud de onda radar (Banda C vs MOLA láser 1064 nm); penetración dieléctrica en costra salina seca | La constante dieléctrica del medio terrestre varía drásticamente por humedad/salmuera; en Marte el medio está completamente seco |
| **3. Morfología (Polígonos y cuencas)** | **Indirecta** (escalado métrico) | Diámetro poligonal ($m$), relación de aspecto, confinamiento topográfico de cuenca (km²) | Terrestre: 10 m (S2) y visual submétrico. Marte: 0.25-0.5 m (HiRISE), 100 m (THEMIS) | **No** para comparación morfométrica en HiRISE; **Sí** para contextualizar con mosaicos regionales | Los polígonos de Uyuni son dinámicos (anuales); los de Terra Sirenum son fósiles y están erosionados por viento eólico durante 3.5 Ga | El estrés térmico diurno en Marte ($\Delta T \approx 100\text{ K}$) y la desecación hiperárida operan sin recarga pluvial contemporánea |
| **4. Tipos de Depósitos** | **Cualitativa** | Facies mineralógicas, costras evaporíticas masivas, eflorescencias salinas | Datos de campo/geológicos en Tierra vs firmas térmicas THEMIS en Marte | N/A (clasificación ontológica tipológica) | Ambigüedad en la identificación de sales accesorias en Marte debido a la baja resolución de THEMIS (100 m/px) | Espesor de la costra: en Uyuni alcanza >10 metros de halita pura; en Terra Sirenum se estiman espesores delgados a métricos |
| **5. Evidencia Mineralógica** | **Indirecta** (espectroscópica) | Terrestre: reflectancia SWIR/VNIR. Marte: DCS térmico (THEMIS $\mu\text{m}$) y parámetros CRISM | S2 (20 m) vs THEMIS (100 m) y CRISM (18-36 m) | **Sí**, integración en celdas espaciales comparables | La halita pura es espectralmente neutra ("plana") en VNIR-SWIR; su detección en Marte requiere confirmación térmica | En Tierra abundan sales de litio, boro y carbonatos por vulcanismo andino; en Marte predominan matrices basálticas con sulfatos de Fe/Mg y cloruros |
| **6. Procesos Evaporíticos** | **Indirecta** (modelado hidrológico) | Tasa de evaporación ($mm/\text{año}$), balance hídrico, concentración salina iónica | Modelos climáticos terrestres vs paleomodelos hidrogeológicos de Marte | N/A (comparación paramétrica conceptual) | Profundidad del manto freático original marciano y duración de la fase lacustre noachiana | Ausencia de ciclo hidrológico activo en Marte moderno; evaporación marciana antigua ocurrió bajo atmósferas con alto $\text{CO}_2$ y baja presión |
| **7. Contexto Ambiental** | **Incompatible / Cualitativa** | Presión (mbar), radiación solar ($W/m^2$), radiación UV ($J/m^2$), flujo térmico | Mediciones in situ vs sensores orbitales y modelos | N/A | Variabilidad paleoclimática marciana no calibrada de forma directa | Presión atmosférica: Uyuni ~600 mbar vs Marte actual ~6-7 mbar; atmósfera terrestre oxidante $N_2/O_2$ vs $\text{CO}_2$ marciano |

---

## 3. ANÁLISIS DETALLADO POR DIMENSIÓN DE COMPARABILIDAD

### 3.1 Pendiente Topográfica ($\nabla z$)
* **Naturaleza de la comparación:** **Directa**. La pendiente local es una cantidad adimensional derivada del gradiente del campo de elevación: $\theta = \arctan\left(\sqrt{(\partial z / \partial x)^2 + (\partial z / \partial y)^2}\right)$.
* **Compatibilidad métrica:** Plenamente compatible en grados angulares (°) o porcentaje tangencial.
* **Resolución y remuestreo:** 
  * En la Tierra, NASADEM proporciona elevación a 30 m/px. En el Salar de Uyuni, la pendiente media del núcleo salino es $< 0.05^\circ$ (desviación vertical $< 0.5\text{ m}$ a lo largo de 50 km).
  * En Marte, MOLA MEG128 posee un tamaño de píxel de ~463 m en el ecuador. Para comparar adecuadamente la cuenca de Terra Sirenum con Uyuni, el modelo terrestre debe agregarse o remuestrearse espacialmente a la resolución de MOLA (o analizarse en el dominio frecuencial/espectral de Fourier a longitudes de onda espaciales $> 1\text{ km}$).
* **Física y límites:** La menor gravedad de Marte ($g = 3.71\text{ m/s}^2$) permite taludes de detritos clásticos ligeramente más empinados antes de alcanzar el colapso gravitatorio. Sin embargo, en fondos de cuencas lacustres/evaporíticas donde opera la sedimentación por gravedad y sedimentación de fluidos en reposo, el plano de sedimentación original es horizontal en ambos planetas.

### 3.2 Rugosidad Superficial
* **Naturaleza de la comparación:** **Indirecta**. La rugosidad depende de la escala espacial a la que se mida ($RMS(L)$ a escala métrica, decamétrica o kilométrica).
* **Compatibilidad de unidades:** 
  * En datos altimétricos: Raíz del error cuadrático medio de alturas ($RMS$ en metros) respecto a un plano local ajustado.
  * En datos radar: Coeficiente de retrodispersión $\sigma^0$ en decibelios (dB). Un salar liso y plano actúa como reflector especular produciendo retrodispersión extremadamente baja (tonos oscuros en radar); una costra salina rugosa con bordes poligonales sobreelevados genera dispersión difusa intensa (tonos brillantes).
* **Diferencias físicas no reducibles:** En la Tierra, la permitividad dieléctrica ($\epsilon$) de los salares está fuertemente modulada por la humedad residual y salmueras hipersalinas subsuperficiales. En Marte actual, el subsuelo de Terra Sirenum es un medio puramente seco y congelado, por lo que la señal de dispersión depende exclusivamente de la rugosidad geométrica y de la constante dieléctrica estática de la halita y roca basáltica ($\epsilon_r \approx 3 - 6$).

### 3.3 Morfología y Polígonos de Desecación
* **Naturaleza de la comparación:** **Indirecta (morfométrica / escalada)**.
* **Observación empírica:** 
  * En el Salar de Uyuni, la contracción durante el secado de la halita y la recristalización inducida por evaporación continua producen redes de polígonos de sal regulares con diámetros que oscilan entre **1 y 3 metros**, con rebordes sobreelevados de 5 a 15 cm.
  * En Terra Sirenum, la observación HiRISE `PSP_003160_1410` documenta depósitos claros fracturados en polígonos de desecación de **1 a 5 metros de diámetro**, confinados estrictamente en depresiones topográficas locales y fondos de paleocanales invertidos.
* **Proceso subyacente:** Ambos fenómenos obedecen a ecuaciones de fracturación por contracción y relajación de esfuerzos de tensión en medios saturados de salmuera que experimentan pérdida de solvente (agua).
* **Incertidumbre crítica:** Los polígonos de Uyuni son morfológicamente activos y se regeneran con el ciclo anual de inundación/evaporación. Los polígonos de Marte son rasgos fósiles de edad Noachiana-Hesperiana que han resistido miles de millones de años de bombardeo micrometeorítico y erosión eólica, manteniéndose visibles gracias a la cementación salina resistente.

### 3.4 Tipos de Depósitos y Evidencia Mineralógica
* **Naturaleza de la comparación:** **Cualitativa / Indirecta**.
* **Detección espectral de cloruros:**
  * El NaCl (halita) puro es químicamente anhidro y posee enlaces iónicos que no presentan modos vibracionales fundamentales activos en el rango del infrarrojo cercano y de onda corta (VNIR-SWIR, 0.4 a 2.5 µm). Por tanto, en sensores como CRISM o Sentinel-2 MSI, la halita pura se presenta como una superficie sin absorciones diagnósticas ("espectralmente plana"), con alta o moderada reflectancia.
  * Su detección inequívoca en Marte descansa en el **infrarrojo térmico (THEMIS)**: a longitudes de onda entre 8 y 14 µm, los silicatos y basaltos circundantes exhiben bandas de absorción vibracional de enlaces Si-O (reststrahlen band), mientras que los cloruros no tienen absorciones en ese intervalo, presentando una emisividad relativamente uniforme. Al aplicar una transformación de descorrelación espectral (DCS) a las bandas 8, 7 y 5 de THEMIS, los depósitos de cloruro resaltan sistemáticamente en coloraciones azul brillante / magenta.
* **Asociación litológica:** En Terra Sirenum, los cloruros se encuentran a menudo estratigráficamente suprayacentes o marginales a depósitos de filosilicatos (arcillas de alteración acuosa alcalina o neutra), lo que sugiere que la precipitación evaporítica de sales de cloruro representó la fase final de desecación de paleolagos o charcas efímeras cerradas. En Uyuni y Lípez, la secuencia evaporítica típica contiene arcillas basales, seguidas de yeso ($CaSO_4 \cdot 2H_2O$), halita masiva ($NaCl$) y salmueras residuales ricas en sulfatos de magnesio, boro y litio.

### 3.5 Contexto Ambiental y Físico
* **Naturaleza de la comparación:** **Incompatible como análogo contemporáneo total; Válido como análogo de estrés extremo localizado**.
* **Gradientes:**
  * **Presión atmosférica:** Uyuni (~600 mbar a 3656 msnm; ~540 mbar en Sol de Mañana a 4850 msnm). Marte contemporáneo (~6 a 7 mbar). Si bien la presión en el Altiplano es la más baja de cuencas evaporíticas continentales terrestres habitadas, sigue siendo dos órdenes de magnitud mayor que la marciana.
  * **Radiación ultravioleta:** El Altiplano boliviano presenta uno de los flujos de radiación UV-B y UV-A más altos de la superficie terrestre (índice UV que puede superar 25-30), debido a la gran altitud, baja columna de ozono y alta reflectancia del suelo. Esto lo convierte en un excelente análogo astrobiológico para estudiar la fotodegradación y supervivencia de biomarcadores en costras salinas.
  * **Ciclo térmico:** En Uyuni y Sol de Mañana, las oscilaciones térmicas día-noche oscilan entre $+25^\circ\text{C}$ diurnos y $-20^\circ\text{C}$ nocturnos en invierno ($\Delta T \approx 45\text{ K}$). En Terra Sirenum, el rango térmico diurno puede variar de $-10^\circ\text{C}$ a $-90^\circ\text{C}$ ($\Delta T \approx 80-100\text{ K}$).

---

## 4. DIRECTRICES DE IMPLEMENTACIÓN PARA EL BACKEND DE ANALOGX

1. **Desacoplamiento estricto de capas:**
   El backend no implementará una función de similitud que mezcle en un único escalar sin fundamento variables incompatibles. Cada comparación debe ser atómica y tipada como `directa`, `indirecta` o `cualitativa`.
2. **Cálculo de relieve relativo dentro de la cuenca:**
   Toda métrica de elevación se normalizará respecto al fondo de la cuenca local:
   $$z_{\text{relativo}}(x,y) = z(x,y) - \min_{(u,v) \in \text{Cuenca}} z(u,v)$$
   Garantizando total invariancia frente al datum Areoide marciano o WGS84 terrestre.
3. **Validación de evidencias:**
   Ningún registro de observación con `verification_status = "pendiente_de_verificar"` podrá alimentar una conclusión científica de compatibilidad sin el flag explícito de incertidumbre.

