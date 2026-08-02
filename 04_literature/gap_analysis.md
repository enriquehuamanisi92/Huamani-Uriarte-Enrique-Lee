# Analisis preliminar de brechas

Estas brechas son proposiciones que la busqueda sistematica debera confirmar, matizar o rechazar. No se presentan como hallazgos definitivos.

| Brecha candidata | Evidencia necesaria | Respuesta del proyecto |
|---|---|---|
| Poca validacion publicada a escala intradistrital en Comas. | Busqueda regional reproducible y consulta de repositorios peruanos. | Estudio localizado con unidad territorio-mes. |
| Predominio de evaluaciones aleatorias que ignoran tiempo o espacio. | Extraer particion y horizonte de cada estudio incluido. | Validacion temporal rodante y espacial agrupada. |
| Comparacion insuficiente con baselines operativamente simples. | Registrar comparadores de cada estudio. | Baselines de prevalencia, persistencia y hotspot historico. |
| Integracion limitada de denuncias, censo y entorno urbano. | Documentar fuentes y granularidades utilizadas. | Pipeline multifuente con trazabilidad y analisis de sensibilidad. |
| Reporte centrado en discriminacion y poco en calibracion/utilidad. | Extraer metricas, calibracion e intervalos. | PR-AUC, Brier, curvas de calibracion, errores e incertidumbre. |
| Riesgos de sesgo y realimentacion tratados de modo superficial. | Evaluar documentacion de equidad, gobernanza y uso. | Auditoria territorial, model card, supervision y criterios de no uso. |
| Baja reproducibilidad de datos y transformaciones. | Verificar codigo, datos, parametros y versiones disponibles. | Scripts, DVC, MLflow curado, hashes y prueba de clon limpio. |

## Contribucion propuesta

La contribucion no sera afirmar que un algoritmo complejo siempre supera a los metodos existentes. Sera evaluar, con un diseno auditable, si la integracion espacio-temporal mejora prediccion y calibracion frente a baselines en Comas, bajo restricciones explicitas de privacidad y uso. Un resultado nulo o un modelo simple superior tambien constituiria evidencia util.

## Criterio de confirmacion

Una brecha solo se trasladara a la introduccion final si la matriz de estudios permite sostenerla. La frase final indicara alcance de bases, fechas, numero de estudios y limitaciones, evitando generalizaciones universales.
