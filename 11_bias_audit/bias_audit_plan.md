# Plan de auditoria de sesgos

## Alcance

En la fase sintetica solo se prueba el procedimiento. Una conclusion de equidad requiere datos reales apropiados, contexto y participacion institucional/comunitaria. Igualdad de metricas no garantiza ausencia de dano.

## Fuentes de sesgo

- Cobertura desigual de denuncia y geocodificacion.
- Cambios en clasificacion o presencia policial.
- Variables territoriales que actuan como proxies de condiciones protegidas.
- Celdas con tamanos pequenos e incertidumbre alta.
- Seleccion de umbral que distribuye falsos positivos y negativos.
- Deriva y realimentacion tras cualquier intervencion.

## Evaluacion preespecificada

1. Describir cobertura y faltantes por sector y tiempo.
2. Comparar prevalencia registrada y tamanos de muestra.
3. Reportar PR-AUC, Brier, calibracion, FPR, FNR, precision y recall por sector con intervalos bootstrap.
4. Evaluar sensibilidad a unidad espacial y umbral.
5. Comparar un modelo con y sin variables potencialmente problematicas.
6. Inspeccionar importancia, errores extremos y estabilidad temporal.
7. Documentar quien asume el costo de cada tipo de error.

No se haran comparaciones de subgrupos con conteos insuficientes. Las categorias territoriales no se presentaran como atributos intrinsecos de sus habitantes.

## Criterios de revision

No se fija una tolerancia universal sin contexto. Antes de un piloto, responsables y representantes pertinentes definiran limites de desempeno y seguridad. Una disparidad persistente, calibracion deficiente o baja cobertura puede exigir recoleccion adicional, modelo separado, mayor agregacion o no uso.

## Monitoreo

Version, periodo, cobertura, deriva de predictores, calibracion y errores se revisaran con una frecuencia definida antes del despliegue. Existira una regla de suspension y un responsable con autoridad para aplicarla.
