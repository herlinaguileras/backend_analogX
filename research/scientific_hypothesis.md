# HIPÓTESIS CIENTÍFICA COMPROBABLE Y METODOLOGÍA DE VALIDACIÓN
## AnalogX — Planetary Analog Discovery Engine (NASA Space Apps Challenge 2026)

> **Documento:** `research/scientific_hypothesis.md`  
> **Versión:** 1.0.0 (Fase 0 — Backend)  
> **Estatus:** Formulación formal aprobada  

---

## 1. PREGUNTA GUÍA CIENTÍFICA

> **¿Qué características morfométricas de los depósitos salinos, de su confinamiento topográfico y de los procesos evaporíticos e hidrotermales terrestres permiten caracterizar, diferenciar y contrastar de manera verificable los depósitos de cloruro antiguos observados en cuencas de las tierras altas del sur de Marte (Terra Sirenum)?**

---

## 2. FORMULACIÓN DE HIPÓTESIS FORMALES

### 2.1 Hipótesis de Trabajo ($H_1$)
> **$H_1$:**  
> "Los depósitos salinos de cloruro identificados en depresiones topográficas locales de Terra Sirenum (Marte, centrados en $\sim 38.8^\circ\text{ S}, 221.0^\circ\text{ E}$) exhiben un conjunto estructurado de propiedades morfométricas y de confinamiento geológico —específicamente:
> 1. Ubicación confinada en mínimos topográficos locales con pendientes basales de cuenca $\nabla z < 1.5^\circ$,
> 2. Variación de relieve relativo local $\Delta z_{\text{rel}} < 15\text{ m}$ sobre longitudes de onda espaciales decamétricas,
> 3. Textura superficial fracturada en redes poligonales de desecación métricas ($1\text{ a }5\text{ m}$ de diámetro), y
> 4. Carencia de bandas diagnósticas de absorción catiónica en el SWIR con contraste de emisividad selectivo en el infrarrojo térmico—  
> que son dimensionalmente y estructuralmente consistentes con patrones de desecación evaporítica endorreica terminal de salmueras terrestres, calibrados en el Salar de Uyuni (como modelo de evaporación pasiva masiva) y complementados por el campo Sol de Mañana (como modelo de alteración hidrotermal previa)."

### 2.2 Hipótesis Nula ($H_0$)
> **$H_0$:**  
> "Los depósitos de cloruro de Terra Sirenum no se diferencian estadísticamente ni morfométricamente del terreno basáltico o de manto eólico circundante en términos de confinamiento topográfico, rugosidad de pendiente relativa y textura poligonal; sus patrones no reflejan procesos evaporíticos análogos a los salares terrestres, siendo explicables como simples alteraciones superficiales eólicas o eyecciones de impacto no confinadas."

---

## 3. CRITERIOS CUANTITATIVOS Y MÉTRICAS COMPROBABLES

Para evitar afirmaciones subjetivas o cualitativas ambiguas, el motor AnalogX evaluará las siguientes **métricas cuantificables**:

### Métrica 1: Índice de Confinamiento Topográfico de Cuenca ($TCI$)
Define si el depósito se ubica en el fondo de una depresión cerrada donde fluidos acuosos pudieron estancarse y evaporarse:
$$TCI = \frac{z_{\text{borde\_medio}} - z_{\text{depósito}}}{\sigma_{z\text{\_local}}}$$
* *Criterio de aceptación análoga:* $TCI > 1.5$ (el depósito se ubica significativamente por debajo del borde de la cuenca receptora, tanto en Uyuni como en Terra Sirenum).

### Métrica 2: Gradiente de Pendiente Basal ($\nabla z$)
Calculado a partir de NASADEM (Tierra) remuestreado y MOLA MEG128 (Marte):
$$\theta = \arctan\left(\sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2}\right)$$
* *Criterio de aceptación análoga:* $\theta_{\text{media}} < 1.0^\circ$ en el fondo del depósito, con incremento abrupto ($\theta > 3^\circ$) en las paredes de confinamiento.

### Métrica 3: Rugosidad Superficial RMS Normalizada ($R_{RMS}$)
Desviación estándar de alturas en una ventana móvil de radio $L_0$:
$$R_{RMS} = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (z_i - \bar{z}_{\text{plano}})^2}$$
* *Criterio de aceptación:* Valores decamétricos de $R_{RMS} < 0.35\text{ m}$ en la costra salina continua frente a $R_{RMS} > 1.2\text{ m}$ en los terrenos volcánicos/craterizados marginales.

### Métrica 4: Escala de Redes Poligonales ($D_{\text{polígono}}$)
Distribución de diámetros mayores de polígonos de desecación medidos en imágenes ortorrectificadas submétricas (Sentinel-2 / ortofotos en Tierra; HiRISE `PSP_003160_1410` en Marte):
* *Rango medido en Uyuni:* $1.2\text{ m} \le D \le 3.5\text{ m}$ (media $\approx 2.1\text{ m}$).
* *Rango medido en HiRISE Terra Sirenum:* $1.5\text{ m} \le D \le 4.8\text{ m}$ (media $\approx 2.8\text{ m}$).
* *Criterio de aceptación:* Concordancia dentro del mismo orden de magnitud métrico ($1\text{ a }5\text{ m}$), con morfología hexagonal a pentagonal dominante originada por fracturación tensional de desecación.

### Métrica 5: Criterio Espectral Térmico vs SWIR (Descarte de Falsos Positivos)
* *En SWIR (CRISM / Sentinel-2):* Ausencia de absorciones profundas en $1.4\text{ }\mu\text{m}$ y $1.9\text{ }\mu\text{m}$ correspondientes a agua estructural libre (a diferencia de yeso o arcillas esmectitas), confirmando el carácter anhidro del cloruro sódico.
* *En Térmico (THEMIS DCS 8-7-5):* Índice de descorrelación térmico elevado en tono azul/magenta en Marte, correspondiente a una emisividad espectralmente neutra frente a la absorción por silicatos circundantes.

---

## 4. METODOLOGÍA DE CONTROLES CIENTÍFICOS Y ESCENARIOS DE FALLA

### 4.1 Áreas de Control Negativo (Falsación)
Para validar que el motor AnalogX no detecte "similitud" en cualquier terreno planetario, se definirán dos **áreas de control negativo**:
1. **Control Negativo Marciano:** Llanuras basálticas sin alteración en Syrtis Major o llanuras eólicas de Cerberus Palus. Si el algoritmo califica a Syrtis Major como análogo de Uyuni, el algoritmo falla.
2. **Control Negativo Terrestre:** Dunas de arena del Desierto de Atacama o coladas basálticas de Hawái. Deben presentar firmas morfométricas y espectrales disyuntas frente a Terra Sirenum.

### 4.2 Escenarios de Rechazo de la Hipótesis ($H_1 \to \text{Rechazada}$)
La hipótesis se considerará falsada si se demuestra que:
1. La pendiente basal del depósito de Terra Sirenum excede significativamente los $5^\circ$ (descartando sedimentación hidrostática de fluidos en reposo).
2. Los rasgos poligonales observados por HiRISE son en realidad dunas transversales eólicas (*megaripples* o TARs) con longitudes de onda no hexagonales.
3. Futuros análisis espectrales demuestran que los depósitos de THEMIS corresponden a vidrio volcánico no hidratado o piroclastos deshidratados en lugar de sales evaporíticas de cloruro.

