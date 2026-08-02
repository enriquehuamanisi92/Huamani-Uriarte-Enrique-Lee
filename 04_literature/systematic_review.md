# Revision exploratoria estructurada de literatura

## Estado y alcance

Este documento es un protocolo y una sintesis exploratoria para el curso. **Todavia no es una revision sistematica concluida.** Los conteos de una version anterior (106 identificados y 12 incluidos) no se presentan como resultados verificables porque el repositorio no contiene las exportaciones, fechas, decisiones por registro ni textos evaluados que permitan auditarlos. El diagrama existente se conserva solo como borrador historico y debera regenerarse despues de ejecutar la busqueda.

## Pregunta de revision

¿Que metodos, fuentes de datos, estrategias de validacion y salvaguardas se han utilizado para predecir riesgo delictivo agregado en territorios urbanos mediante aprendizaje automatico y analisis geoespacial, y que evidencia existe en contextos latinoamericanos comparables con Comas?

## Protocolo de busqueda planificado

| Elemento | Decision preespecificada |
|---|---|
| Bases | Scopus, Web of Science, IEEE Xplore, ACM Digital Library y SciELO; busqueda complementaria en Google Scholar y organismos oficiales. |
| Periodo | 2008 hasta la fecha de ejecucion final. |
| Idiomas | Ingles, espanol y portugues. |
| Fecha de busqueda | **Pendiente de ejecutar y registrar.** |
| Gestion | Exportar RIS/BibTeX/CSV; conservar consulta, fecha, filtros y total por base; deduplicar por DOI, titulo y autores. |
| Reporte | Flujo inspirado en PRISMA 2020, sin afirmar cumplimiento hasta completar su lista de verificacion. |

### Consulta conceptual

```text
("crime prediction" OR "crime risk" OR "predictive policing" OR
 "crime forecasting" OR "urban safety")
AND ("machine learning" OR "statistical learning" OR "deep learning")
AND (geospatial OR spatial OR spatiotemporal OR GIS OR hotspot)
AND (urban OR city OR district OR municipal)
```

La consulta se adaptara a la sintaxis de cada base y se guardara literalmente en `search_log.csv`.

## Elegibilidad

### Inclusion

- Estudios de riesgo, incidencia o concentracion delictiva a escala territorial urbana.
- Modelos estadisticos, de ML o espacio-temporales con validacion fuera de muestra.
- Descripcion suficiente de datos, unidad espacial, horizonte y metricas.
- Estudios empiricos, revisiones metodologicas y documentos de gobernanza directamente pertinentes.

### Exclusion

- Prediccion individual de autor, reincidencia, culpabilidad o perfiles personales.
- Trabajos sin evaluacion empirica cuando se analice desempeno predictivo.
- Estudios sin acceso a texto o informacion minima tras intentar recuperarla.
- Duplicados, resumenes sin articulo y trabajos fuera del ambito urbano-territorial.

Dos revisores serian deseables para titulo/resumen y texto completo. Si el curso solo permite un revisor, se declarara esa limitacion y una muestra de decisiones sera verificada por una segunda persona sin atribuir una revision inexistente.

## Extraccion y calidad

Por estudio se registraran: referencia/DOI, pais, periodo, fuente, unidad espacial y temporal, delito, resultado, predictores, modelo, baseline, particion, prevencion de fuga, metricas, calibracion, validacion externa, explicabilidad, equidad y limitaciones. La calidad se evaluara con criterios predefinidos de representatividad, temporalidad, transparencia, comparador, generalizacion y riesgo de sesgo; no se fabricara una puntuacion retrospectiva.

## Sintesis exploratoria verificable

La literatura fundacional sugiere que la concentracion del delito y la dependencia espacio-temporal pueden sustentar pronosticos territoriales, pero la utilidad depende del comparador y del diseno de validacion. Los registros policiales no son una fotografia neutral: reflejan ocurrencia, denuncia y practicas institucionales. Por ello, la precision no elimina riesgos de realimentacion y distribucion desigual de vigilancia.

Para Comas se derivan cinco compromisos:

1. Comparar el ML con baselines de persistencia y hotspots historicos.
2. Separar entrenamiento, ajuste y prueba respetando el tiempo.
3. Medir transferencia espacial a territorios no vistos.
4. Reportar calibracion, incertidumbre y errores territoriales, no solo AUC.
5. Tratar el producto como apoyo agregado y no como automatizacion policial.

## Referencias semilla (verificadas por DOI o editor)

- Chainey, S., Tompson, L., & Uhlig, S. (2008). The utility of hotspot mapping for predicting spatial patterns of crime. *Security Journal, 21*, 4-28. https://doi.org/10.1057/palgrave.sj.8350066
- Mohler, G. O., Short, M. B., Brantingham, P. J., Schoenberg, F. P., & Tita, G. E. (2011). Self-exciting point process modeling of crime. *Journal of the American Statistical Association, 106*(493), 100-108. https://doi.org/10.1198/jasa.2011.ap09546
- Perry, W. L., McInnis, B., Price, C. C., Smith, S. C., & Hollywood, J. S. (2013). *Predictive Policing: The Role of Crime Forecasting in Law Enforcement Operations*. RAND. https://doi.org/10.7249/RR233
- Lum, K., & Isaac, W. (2016). To predict and serve? *Significance, 13*(5), 14-19. https://doi.org/10.1111/j.1740-9713.2016.00960.x
- Meijer, A., & Wessels, M. (2019). Predictive policing: Review of benefits and drawbacks. *International Journal of Public Administration, 42*(12), 1031-1039. https://doi.org/10.1080/01900692.2019.1575664
- Richardson, R., Schultz, J. M., & Crawford, K. (2019). Dirty data, bad predictions. *New York University Law Review Online, 94*, 15-55.
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Estas referencias son un conjunto inicial, no equivalen a los estudios incluidos de una revision terminada.
