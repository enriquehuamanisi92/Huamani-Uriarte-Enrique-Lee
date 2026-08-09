# 04. Revisión de literatura

Esta carpeta documenta la revisión exploratoria de literatura del proyecto doctoral sobre predicción territorial del riesgo delictivo mediante aprendizaje automático y análisis geoespacial, con aplicación prevista en el distrito de Comas, Lima.

## Pregunta de revisión

¿Qué métodos, fuentes de datos, estrategias de validación y salvaguardas se han utilizado para predecir el riesgo agregado de delincuencia urbana mediante aprendizaje automático y análisis geoespacial, y qué evidencia existe en contextos latinoamericanos comparables con Comas?

## Contenido de la carpeta

| Archivo | Contenido |
|---|---|
| [`systematic_review.md`](systematic_review.md) | Protocolo de búsqueda, criterios de elegibilidad, estrategia de extracción y síntesis exploratoria. |
| [`prisma_2020_flow.md`](prisma_2020_flow.md) | Hoja de trabajo alineada con el diagrama PRISMA 2020, conteos y controles de consistencia. |
| [`gap_analysis.md`](gap_analysis.md) | Brechas preliminares, evidencia necesaria para confirmarlas y respuesta propuesta del proyecto. |
| [`search_log.csv`](search_log.csv) | Bitácora reproducible para registrar consultas, fechas, filtros y resultados por base de datos. |
| [`screening_log.csv`](screening_log.csv) | Registro de deduplicación y decisiones de selección por título, resumen y texto completo. |
| [`evidence_extraction.csv`](evidence_extraction.csv) | Matriz para extraer métodos, datos, validación, métricas, calibración, equidad y limitaciones. |

## Alcance y estado actual

La revisión se encuentra en fase de protocolo y síntesis exploratoria. Las búsquedas formales en Scopus, Web of Science, IEEE Xplore, ACM Digital Library y SciELO están pendientes de ejecución y registro. Google Scholar se empleará solo como fuente complementaria.

En consecuencia, todavía no se reportan cantidades definitivas de registros identificados, excluidos o incluidos. Tampoco se presenta un diagrama PRISMA como resultado final hasta disponer de exportaciones de las bases de datos, fechas de búsqueda, decisiones por registro y textos evaluados. Esta decisión evita presentar como evidencia cifras que no puedan auditarse.

## Hallazgos preliminares

La literatura semilla sugiere que la concentración espacial y la dependencia temporal del delito pueden apoyar pronósticos territoriales. Sin embargo, el valor práctico de un modelo depende de la calidad de sus comparadores, del respeto del orden temporal durante la validación y de su capacidad para generalizar a territorios no observados.

Los registros policiales tampoco constituyen una medición neutral: combinan ocurrencia, denuncia y prácticas institucionales. Por ello, una buena exactitud predictiva no elimina los riesgos de vigilancia desigual, sesgo territorial o ciclos de retroalimentación.

La revisión orienta cinco compromisos metodológicos para el estudio:

1. Comparar los modelos de aprendizaje automático con líneas base de prevalencia, persistencia y puntos calientes históricos.
2. Separar entrenamiento, ajuste y prueba preservando el orden temporal.
3. Evaluar transferencia espacial en territorios no utilizados para el entrenamiento.
4. Reportar calibración, incertidumbre y errores territoriales, además de métricas de discriminación.
5. Limitar los resultados a apoyo agregado para decisiones, nunca a la predicción de personas ni a la vigilancia automatizada.

## Brechas que debe confirmar la búsqueda

- Escasa validación publicada a escala intradistrital en Comas y contextos peruanos comparables.
- Uso frecuente de particiones aleatorias que ignoran la estructura temporal o espacial.
- Comparación insuficiente con líneas base operativamente simples.
- Integración limitada y poco documentada de denuncias, datos censales y contexto urbano.
- Énfasis en discriminación predictiva, con menor atención a calibración, incertidumbre y utilidad.
- Tratamiento superficial de sesgos, efectos de retroalimentación y límites de uso.
- Baja reproducibilidad de transformaciones, parámetros y procedencia de datos.

Estas brechas son hipótesis de trabajo, no conclusiones definitivas. Solo se incorporarán como aportes confirmados cuando estén respaldadas por la matriz de evidencia completa.

## Referencias semilla verificadas

- Chainey, S., Tompson, L., & Uhlig, S. (2008). *The utility of hotspot mapping for predicting spatial patterns of crime*. Security Journal, 21, 4–28. https://doi.org/10.1057/palgrave.sj.8350066
- Mohler, G. O., et al. (2011). *Self-exciting point process modeling of crime*. Journal of the American Statistical Association, 106(493), 100–108. https://doi.org/10.1198/jasa.2011.ap09546
- Perry, W. L., et al. (2013). *Predictive Policing: The Role of Crime Forecasting in Law Enforcement Operations*. RAND. https://doi.org/10.7249/RR233
- Lum, K., & Isaac, W. (2016). *To predict and serve?* Significance, 13(5), 14–19. https://doi.org/10.1111/j.1740-9713.2016.00960.x
- Meijer, A., & Wessels, M. (2019). *Predictive policing: Review of benefits and drawbacks*. International Journal of Public Administration, 42(12), 1031–1039. https://doi.org/10.1080/01900692.2019.1575664
- Richardson, R., Schultz, J. M., & Crawford, K. (2019). *Dirty data, bad predictions*. New York University Law Review Online, 94, 15–55.
- Page, M. J., et al. (2021). *The PRISMA 2020 statement*. BMJ, 372, n71. https://doi.org/10.1136/bmj.n71

Estas publicaciones constituyen referencias iniciales; no equivalen al conjunto final de estudios incluidos.

## Próximo paso

Ejecutar las búsquedas, conservar las exportaciones originales, completar las bitácoras y construir el flujo PRISMA y la síntesis final únicamente a partir de evidencia trazable.
