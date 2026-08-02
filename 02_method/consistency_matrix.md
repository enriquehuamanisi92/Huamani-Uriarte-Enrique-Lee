# Matriz de consistencia

## Formulacion central

| Elemento | Formulacion operacional |
|---|---|
| Problema | La gestion preventiva en Comas dispone principalmente de informacion retrospectiva y fragmentada; no se ha validado localmente un modelo espacio-temporal que integre denuncias, atributos censales y entorno urbano para estimar riesgo del periodo siguiente. |
| Pregunta general | ¿En que medida un modelo integrado predice el riesgo mensual de delitos patrimoniales por unidad territorial, frente a baselines historicos, bajo validacion temporal y espacial? |
| Objetivo general | Desarrollar y validar un modelo de ML y analisis geoespacial para estimar el riesgo delictivo mensual y producir salidas agregadas utiles para gestion preventiva responsable. |
| Hipotesis general | El modelo integrado presenta mejor discriminacion y utilidad predictiva fuera de muestra que un baseline basado solo en incidencia historica, sin deterioro sustantivo de calibracion entre sectores territoriales. |
| Unidad de analisis propuesta | Unidad territorial agregada de Comas por mes. La geometria definitiva (manzana agrupada, cuadrilla o hexagono H3) se fijara con la calidad y restricciones de los datos autorizados. |
| Poblacion de estudio | Observaciones territorio-mes de Comas durante 2018-2025 que cumplan reglas de calidad, geocodificacion y privacidad. |

## Correspondencia de objetivos, variables y analisis

| Objetivo especifico | Variable o evidencia | Indicador | Analisis previsto |
|---|---|---|---|
| OE1. Construir una base espacio-temporal documentada. | Denuncias agregadas, censo y entorno urbano. | Completitud, duplicados, geocodificacion, consistencia temporal. | Perfilamiento, reglas de calidad y analisis de faltantes. |
| OE2. Caracterizar patrones espaciales y temporales. | Conteo y tasa de delitos patrimoniales. | Tendencia, estacionalidad, Moran global/local. | Series temporales, mapas y autocorrelacion espacial. |
| OE3. Entrenar modelos y baselines. | Predictores conocidos hasta el mes t. | Probabilidad o riesgo para t+1. | Regresion logistica, modelos de arboles y baseline de persistencia. |
| OE4. Validar generalizacion. | Predicciones fuera de muestra. | PR-AUC, ROC-AUC, Brier, calibracion, precision, recall y F1. | Ventanas temporales rodantes y particiones espaciales por grupos. |
| OE5. Examinar interpretabilidad y sesgo. | Errores y explicaciones por sector. | FNR, FPR, calibracion, SHAP/permutacion. | Analisis estratificado con intervalos de confianza. |
| OE6. Traducir resultados a apoyo preventivo. | Mapas agregados y escenarios. | Legibilidad, estabilidad y utilidad con supervision humana. | Evaluacion tecnica y, si se autoriza, validacion con expertos. |

## Variables principales

| Rol | Variable | Definicion preliminar | Escala/fuente |
|---|---|---|---|
| Resultado primario | Incidencia delictiva del mes siguiente | Conteo o tasa de denuncias patrimoniales en t+1; la categorizacion de riesgo sera secundaria. | SIDPOL autorizado, agregado por territorio-mes. |
| Predictora temporal | Historia reciente | Rezagos de 1, 3, 6 y 12 meses, tendencia y estacionalidad, sin usar informacion futura. | Derivada de denuncias. |
| Predictora socioeconomica | Vulnerabilidad territorial | Indice preespecificado a partir de variables censales, documentando vigencia temporal. | Censo Nacional 2017/INEI. |
| Predictora urbana | Exposicion y entorno | Densidad comercial, conectividad, iluminacion u otros indicadores disponibles. | Cartografia y registros oficiales. |
| Estratificacion | Sector territorial | Agrupacion espacial usada para examinar estabilidad y disparidad de error. | Cartografia oficial. |

La definicion final se congelara antes de evaluar el conjunto de prueba. No se convertira un percentil sintetico en umbral institucional sin justificacion empirica y participacion de responsables autorizados.
