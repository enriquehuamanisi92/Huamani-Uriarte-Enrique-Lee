# Revisión sistemática de la literatura (RSL)

## Aprendizaje automático y análisis geoespacial para la predicción territorial del riesgo delictivo urbano

**Autor:** Enrique Lee Huamani Uriarte

**Programa:** Doctorado

**Ámbito de aplicación:** distrito de Comas, Lima Metropolitana, Perú

**Versión:** protocolo RSL 1.0 — agosto de 2026
**Guía de reporte:** PRISMA 2020

> **Estado de la evidencia.** Este documento contiene el protocolo completo y una síntesis exploratoria sustentada en literatura semilla. La búsqueda sistemática, la deduplicación y el cribado todavía deben ejecutarse. Por ello, los conteos PRISMA y las conclusiones definitivas permanecen pendientes. Esta precisión protege la integridad académica y permite presentar claramente qué está terminado y qué falta realizar.

## Resumen

La concentración espacial y temporal de los delitos ha motivado el desarrollo de métodos estadísticos, geoespaciales y de aprendizaje automático para apoyar la gestión preventiva. Sin embargo, su desempeño depende de la calidad de los registros, la unidad territorial, el horizonte de predicción, las líneas base y la validación empleada. Además, los registros de denuncias reflejan tanto la ocurrencia de hechos como la propensión a denunciar y las prácticas institucionales. El objetivo de esta RSL es identificar y sintetizar métodos, fuentes de datos, estrategias de validación, métricas, mecanismos de explicabilidad y salvaguardas éticas utilizados en la predicción agregada del riesgo delictivo urbano, con énfasis en evidencia latinoamericana y contextos comparables con Comas. Se seguirá PRISMA 2020; se consultarán Scopus, Web of Science, IEEE Xplore, ACM Digital Library y SciELO, con búsqueda complementaria en Google Scholar. La síntesis preliminar indica la necesidad de comparar modelos complejos con líneas base simples, preservar el orden temporal, evaluar transferencia espacial, reportar calibración e incertidumbre y controlar riesgos de sesgo y retroalimentación. Estos resultados deberán confirmarse mediante la búsqueda y matriz de evidencia definitivas.

**Palabras clave:** delincuencia urbana; predicción del delito; aprendizaje automático; análisis geoespacial; riesgo territorial; ciudades inteligentes; PRISMA.

## 1. Introducción

La delincuencia urbana presenta concentración espacial, recurrencia temporal y asociación con características del entorno. Estas regularidades permiten formular modelos que estiman el riesgo del siguiente periodo para unidades territoriales agregadas. Tales modelos pueden apoyar la priorización preventiva, pero no deben interpretarse como predicciones de personas, culpabilidad o causalidad.

El problema científico no consiste únicamente en alcanzar una métrica elevada. Un modelo útil debe demostrar que mejora líneas base razonables, que generaliza a periodos futuros y territorios no observados, que está calibrado y que sus errores no se concentran injustificadamente en determinados sectores. En Comas, además, se requiere evidencia local o regional que justifique las decisiones sobre datos, granularidad, validación y gobernanza.

Esta RSL organiza el conocimiento relevante para el proyecto doctoral «Desarrollo y validación de un modelo de predicción del riesgo delictivo urbano basado en aprendizaje automático y análisis geoespacial para la gestión preventiva en Comas, Lima Metropolitana».

## 2. Objetivos y preguntas de revisión

### 2.1 Objetivo general

Identificar, evaluar y sintetizar la evidencia sobre métodos de aprendizaje automático y análisis geoespacial utilizados para predecir riesgo delictivo urbano agregado, considerando desempeño, validación, reproducibilidad, explicabilidad, sesgos y aplicabilidad a Comas.

### 2.2 Objetivos específicos

1. Caracterizar las fuentes de datos, delitos, unidades espaciales, unidades temporales y horizontes de predicción.
2. Comparar algoritmos, ingeniería de variables y líneas base utilizadas.
3. Examinar las estrategias de validación temporal, espacial y externa.
4. Identificar las métricas de discriminación, calibración, utilidad e incertidumbre reportadas.
5. Analizar transparencia, reproducibilidad, privacidad, equidad y riesgos de retroalimentación.
6. Determinar brechas de evidencia para Perú, Lima Metropolitana y Comas.

### 2.3 Pregunta principal

¿Qué métodos, fuentes de datos, estrategias de validación y salvaguardas se han utilizado para predecir el riesgo agregado de delincuencia urbana mediante aprendizaje automático y análisis geoespacial, y qué evidencia existe en contextos latinoamericanos comparables con Comas?

### 2.4 Preguntas secundarias

- **RQ1:** ¿Qué tipos de datos y escalas espaciotemporales se utilizan?
- **RQ2:** ¿Qué modelos y líneas base presentan los estudios?
- **RQ3:** ¿Cómo se evita la fuga de información y se evalúa la generalización futura y territorial?
- **RQ4:** ¿Qué métricas, métodos de calibración y estimaciones de incertidumbre se reportan?
- **RQ5:** ¿Qué medidas de explicabilidad, privacidad, equidad y supervisión humana se incorporan?
- **RQ6:** ¿Qué limitaciones impiden transferir la evidencia disponible al contexto de Comas?

## 3. Metodología

### 3.1 Diseño y estándar

Se realizará una revisión sistemática con síntesis narrativa y tabular, informada por PRISMA 2020. Debido a la heterogeneidad esperada en delitos, escalas, horizontes y métricas, no se presupone un metaanálisis. Su viabilidad se evaluará después de la extracción.

### 3.2 Marco PICOC adaptado

| Elemento | Definición operacional |
|---|---|
| Población/problema | Delitos o denuncias agregados en espacios urbanos. |
| Intervención | Modelos estadísticos, aprendizaje automático o aprendizaje profundo con componentes espaciales o espaciotemporales. |
| Comparación | Persistencia, prevalencia, promedio histórico, hotspot histórico u otros modelos. |
| Resultados | Desempeño predictivo, calibración, utilidad, generalización, explicabilidad, equidad y reproducibilidad. |
| Contexto | Ciudades, distritos, sectores, cuadrículas u otras unidades territoriales; prioridad analítica para América Latina. |

### 3.3 Fuentes de información

Se consultarán Scopus, Web of Science Core Collection, IEEE Xplore, ACM Digital Library y SciELO. Google Scholar y repositorios oficiales se utilizarán como búsqueda complementaria. También se revisarán las referencias de los artículos incluidos. La fecha exacta, filtros, consulta y cantidad exportada de cada fuente se registrarán en `search_log.csv`.

### 3.4 Periodo e idiomas

- Periodo de publicación: enero de 2008 hasta la fecha final de búsqueda.
- Idiomas: español, inglés y portugués.
- Tipos documentales: artículos, trabajos completos de conferencia, revisiones metodológicas pertinentes e informes técnicos o de gobernanza con autoría institucional identificable.

### 3.5 Estrategia de búsqueda

Consulta conceptual base:

```text
("crime prediction" OR "crime forecasting" OR "crime risk" OR
 "predictive policing" OR "urban safety" OR "predicción del delito" OR
 "riesgo delictivo")
AND
("machine learning" OR "deep learning" OR "statistical learning" OR
 "aprendizaje automático")
AND
(geospatial OR spatial OR spatiotemporal OR GIS OR hotspot OR
 geoespacial OR espacial OR espaciotemporal)
AND
(urban OR city OR district OR municipal OR urbano OR ciudad OR distrito)
```

La cadena se adaptará a la sintaxis de cada base sin modificar sus conceptos centrales. Para recuperar evidencia regional se realizará una consulta complementaria con `Peru OR Perú OR Lima OR "Latin America" OR Latinoamérica`. No se presentará una cadena como ejecutada hasta registrar la fecha y el resultado real.

### 3.6 Criterios de inclusión

1. Estudio empírico sobre predicción, pronóstico o estimación futura de delito o riesgo delictivo urbano agregado.
2. Uso de métodos estadísticos predictivos, aprendizaje automático, aprendizaje profundo o análisis espaciotemporal.
3. Evaluación fuera de muestra o descripción suficiente para determinar el diseño de validación.
4. Identificación de fuente de datos, unidad espacial, unidad temporal u horizonte de predicción.
5. Texto completo disponible en español, inglés o portugués.

### 3.7 Criterios de exclusión

1. Predicción individual de reincidencia, autoría, culpabilidad o comportamiento personal.
2. Estudios exclusivamente descriptivos sin componente predictivo, salvo revisiones o documentos de gobernanza directamente relevantes.
3. Contextos no urbanos sin transferibilidad justificada.
4. Resúmenes, presentaciones, editoriales, noticias o textos sin método evaluable.
5. Duplicados o versiones preliminares cuando exista una versión final más completa.
6. Textos cuyo documento completo no pueda recuperarse después de intentos documentados.

### 3.8 Gestión y selección de registros

Los resultados se exportarán en RIS, BibTeX o CSV y se conservarán sin modificación. La deduplicación combinará DOI, título normalizado, autores y año. El cribado tendrá dos etapas: título/resumen y texto completo. Cada exclusión a texto completo tendrá una razón única y documentada en `screening_log.csv`.

Se recomienda que dos revisores evalúen independientemente los registros y resuelvan discrepancias por consenso. Si el trabajo debe realizarlo un solo investigador, se declarará esta limitación y, cuando sea posible, un segundo revisor verificará una muestra. No se afirmará revisión doble si no ocurrió.

### 3.9 Extracción de datos

Se utilizará `evidence_extraction.csv` para registrar: referencia, país, periodo, fuente de datos, tipo de delito, escalas espacial y temporal, objetivo, predictores, modelos, línea base, partición, control de fuga, métricas, calibración, validación externa, explicabilidad, equidad, hallazgo principal y limitaciones.

### 3.10 Evaluación de calidad y riesgo de sesgo

Cada estudio empírico recibirá una valoración `Sí`, `Parcial`, `No` o `No aplica` en los siguientes dominios:

| Dominio | Pregunta de evaluación |
|---|---|
| Representatividad | ¿La procedencia, cobertura y limitaciones de los datos están descritas? |
| Temporalidad | ¿Los predictores están disponibles antes del resultado y se evita fuga de información? |
| Comparadores | ¿Se incluyen líneas base pertinentes y se comparan en las mismas particiones? |
| Validación | ¿La evaluación respeta tiempo/espacio y utiliza datos fuera de muestra? |
| Métricas | ¿Las métricas son apropiadas y se reportan calibración o incertidumbre? |
| Generalización | ¿Se discute transferencia temporal, espacial o externa? |
| Transparencia | ¿Datos, código, parámetros o transformaciones están suficientemente documentados? |
| Impacto y equidad | ¿Se analizan sesgo, privacidad, retroalimentación y límites de uso? |

No se calculará una puntuación total que oculte fallas críticas. Los dominios se reportarán individualmente.

### 3.11 Síntesis

Los estudios se agruparán por enfoque de modelado, escala espacial, horizonte temporal, fuente de datos y región. Se compararán resultados solo cuando las definiciones y particiones sean compatibles. La síntesis distinguirá desempeño aparente, validación temporal, transferencia espacial y validación externa. Se realizará un análisis específico de estudios latinoamericanos.

## 4. Flujo PRISMA 2020

El diagrama proporcionado requiere los siguientes conteos. La hoja operativa está en `prisma_2020_flow.md`.

| Etapa | Conteo |
|---|---:|
| Registros identificados en bases de datos | Pendiente |
| Registros identificados en registros u otras fuentes | Pendiente |
| Duplicados eliminados | Pendiente |
| Registros eliminados por automatización | 0, salvo que se documente su uso |
| Registros eliminados por otras razones antes del cribado | Pendiente |
| Registros cribados por título y resumen | Pendiente |
| Registros excluidos en cribado | Pendiente |
| Informes buscados para recuperación | Pendiente |
| Informes no recuperados | Pendiente |
| Informes evaluados a texto completo | Pendiente |
| Informes excluidos, por razón | Pendiente |
| Estudios incluidos en la revisión | Pendiente |
| Informes correspondientes a estudios incluidos | Pendiente |

## 5. Síntesis exploratoria de literatura semilla

### 5.1 Concentración y predicción espaciotemporal

Chainey, Tompson y Uhlig (2008) evaluaron la utilidad predictiva de técnicas de mapeo de puntos calientes y mostraron que no basta con visualizar concentraciones históricas: su valor debe comprobarse sobre eventos posteriores. Mohler et al. (2011) aplicaron procesos puntuales autoexcitados para representar el riesgo de repetición cercana, reforzando la importancia de la dependencia espacial y temporal.

Para el proyecto de Comas, estos aportes justifican variables históricas rezagadas y análisis de concentración, pero también exigen comparar el aprendizaje automático con un hotspot histórico y con persistencia. Un mapa retrospectivo no equivale por sí mismo a un modelo prospectivo validado.

### 5.2 Evaluación y utilidad operativa

Perry et al. (2013) sitúan el pronóstico del delito como una herramienta dentro de un proceso de decisión más amplio. La predicción no determina automáticamente la intervención ni demuestra su eficacia. En consecuencia, la evaluación del proyecto debe separar desempeño del modelo, utilidad para la planificación y efectos de cualquier intervención futura.

### 5.3 Calidad de datos, sesgo y retroalimentación

Lum e Isaac (2016) y Richardson, Schultz y Crawford (2019) advierten que los datos policiales pueden reproducir patrones de vigilancia y denuncia. Si el despliegue institucional se concentra donde el sistema ya observa más, los nuevos datos pueden reforzar esa concentración. Meijer y Wessels (2019) sintetizan beneficios potenciales y riesgos de gobernanza de la policía predictiva.

Estas advertencias son centrales para Comas: las denuncias no deben interpretarse como medida completa del delito; se deben documentar cobertura, cambios administrativos y subregistro; y el producto debe limitarse a riesgo territorial agregado bajo supervisión humana.

### 5.4 Transparencia del proceso de revisión

Page et al. (2021) establecen PRISMA 2020 como guía para transparentar identificación, selección, exclusión e inclusión. Aplicarlo significa conservar búsquedas exactas, exportaciones, decisiones por registro y razones de exclusión. Un diagrama con cifras no verificables no cumple esa finalidad.

## 6. Brechas preliminares y aporte esperado

La búsqueda sistemática deberá confirmar, refinar o rechazar las siguientes brechas:

1. Evidencia limitada de validación intradistrital en Perú y específicamente en Comas.
2. Uso de particiones aleatorias que pueden sobreestimar el desempeño al ignorar tiempo y espacio.
3. Comparación insuficiente con prevalencia, persistencia y hotspot histórico.
4. Poca atención a calibración, intervalos de incertidumbre y utilidad operativa.
5. Documentación incompleta de procedencia, transformaciones y disponibilidad temporal de variables.
6. Evaluación limitada de disparidades territoriales, privacidad y ciclos de retroalimentación.

El aporte propuesto no presupone que un algoritmo complejo será superior. Consiste en evaluar de forma auditable si la integración espaciotemporal mejora la predicción y calibración frente a líneas base simples en Comas, bajo controles explícitos de privacidad, equidad y uso. Un resultado nulo o la superioridad de un modelo simple también constituirán evidencia útil.

## 7. Implicaciones para el protocolo doctoral

La síntesis preliminar conduce a las siguientes decisiones:

1. Unidad de análisis agregada territorio-mes; nunca predicción individual.
2. Predictores disponibles hasta el cierre del mes anterior al resultado.
3. Ventanas temporales expansivas y periodo final de prueba intacto.
4. Validación espacial agrupada en territorios no utilizados para entrenar.
5. Líneas base de prevalencia, persistencia y hotspot histórico.
6. PR-AUC, Brier, calibración, errores territoriales e intervalos, además de ROC-AUC.
7. Auditoría de procedencia, subregistro, cobertura, fuga y disparidades.
8. Resultados como apoyo a decisiones con supervisión, límites de uso y revisión ética.

## 8. Limitaciones de esta versión

La versión actual no permite afirmar exhaustividad, estimar el número de estudios ni cuantificar tendencias. La literatura semilla fue seleccionada por relevancia conceptual y no mediante el proceso completo de búsqueda y cribado. La síntesis puede cambiar después de ejecutar el protocolo. Estas limitaciones deben indicarse durante la presentación académica.

## 9. Conclusión provisional

La evidencia inicial respalda la viabilidad conceptual de pronósticos territoriales basados en dependencia espaciotemporal, pero no garantiza utilidad local. Para producir evidencia válida en Comas se requiere una RSL trazable y, posteriormente, validación temporal y espacial con datos autorizados. El desempeño debe interpretarse junto con calibración, incertidumbre, calidad de datos, equidad y gobernanza. La conclusión definitiva se redactará únicamente después de completar el flujo PRISMA y la matriz de extracción.

## Referencias semilla

Chainey, S., Tompson, L., & Uhlig, S. (2008). The utility of hotspot mapping for predicting spatial patterns of crime. *Security Journal, 21*, 4–28. https://doi.org/10.1057/palgrave.sj.8350066

Lum, K., & Isaac, W. (2016). To predict and serve? *Significance, 13*(5), 14–19. https://doi.org/10.1111/j.1740-9713.2016.00960.x

Meijer, A., & Wessels, M. (2019). Predictive policing: Review of benefits and drawbacks. *International Journal of Public Administration, 42*(12), 1031–1039. https://doi.org/10.1080/01900692.2019.1575664

Mohler, G. O., Short, M. B., Brantingham, P. J., Schoenberg, F. P., & Tita, G. E. (2011). Self-exciting point process modeling of crime. *Journal of the American Statistical Association, 106*(493), 100–108. https://doi.org/10.1198/jasa.2011.ap09546

Page, M. J., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Perry, W. L., McInnis, B., Price, C. C., Smith, S. C., & Hollywood, J. S. (2013). *Predictive policing: The role of crime forecasting in law enforcement operations*. RAND Corporation. https://doi.org/10.7249/RR233

Richardson, R., Schultz, J. M., & Crawford, K. (2019). Dirty data, bad predictions: How civil rights violations impact police data, predictive policing systems, and justice. *New York University Law Review Online, 94*, 15–55.

## Anexo A. Archivos de trazabilidad

- `search_log.csv`: búsqueda exacta y exportaciones por base.
- `screening_log.csv`: decisiones por registro y razones de exclusión.
- `evidence_extraction.csv`: características y resultados de cada estudio.
- `gap_analysis.md`: brechas sujetas a confirmación.
- `prisma_2020_flow.md`: conteos y controles aritméticos del diagrama PRISMA.
