# Protocolo de investigacion v1.0

**Titulo:** Desarrollo y validacion de un modelo de prediccion del riesgo delictivo urbano basado en aprendizaje automatico y analisis geoespacial para la gestion preventiva en Comas, Lima Metropolitana

**Version:** 1.0 — agosto de 2026

**Autor:** Enrique Lee Huamani Uriarte

## 1. Planteamiento del problema

Las denuncias policiales, los indicadores censales y la informacion del entorno urbano describen dimensiones complementarias del riesgo delictivo, pero suelen encontrarse separadas, con distinta granularidad espacial y periodicidad. El uso exclusivo de reportes retrospectivos limita la evaluacion anticipada de concentraciones territoriales. El problema cientifico-tecnologico es la falta de una validacion local, reproducible y responsable de un modelo que estime el riesgo del periodo siguiente sin confundir denuncia registrada con totalidad de delitos ni convertir correlaciones en explicaciones causales.

El estudio se limita a delitos patrimoniales agregados territorialmente. No busca predecir individuos, reincidencia, culpabilidad ni comportamiento personal. La unidad exacta se seleccionara luego de evaluar cobertura, error de geocodificacion y riesgo de reidentificacion.

## 2. Justificacion

- **Cientifica:** evaluara si la integracion de informacion espacio-temporal aporta generalizacion frente a baselines simples.
- **Tecnologica:** producira un pipeline versionado y un prototipo validado en laboratorio, sujeto a la evaluacion TRL aplicable.
- **Practica:** generara estimaciones agregadas que podrian apoyar priorizacion preventiva bajo supervision humana.
- **Social y etica:** incorporara limites de uso, privacidad, auditoria de disparidades y comunicacion de incertidumbre desde el diseno.

## 3. Preguntas, objetivos e hipotesis

### 3.1 Pregunta general

¿En que medida un modelo que integra antecedentes delictivos, variables socioeconomicas y caracteristicas geoespaciales predice el riesgo mensual de delitos patrimoniales por unidad territorial de Comas, frente a baselines historicos, bajo validacion temporal y espacial?

### 3.2 Objetivo general

Desarrollar y validar el modelo integrado, evaluar discriminacion, calibracion, utilidad y estabilidad territorial, y documentar las salvaguardas necesarias para su uso como apoyo preventivo.

### 3.3 Objetivos especificos

1. Integrar y documentar una base territorio-mes con controles de calidad y trazabilidad.
2. Describir distribucion, tendencia, estacionalidad y autocorrelacion espacial.
3. Comparar modelos supervisados con baselines de prevalencia y persistencia historica.
4. Evaluar generalizacion mediante ventanas temporales rodantes y particiones espaciales.
5. Analizar calibracion, errores, interpretabilidad y disparidades territoriales.
6. Producir mapas agregados, ficha del modelo y protocolo de uso responsable.

### 3.4 Hipotesis

**H1:** el modelo integrado superara al baseline historico en PR-AUC y Brier score en periodos futuros.

**H2:** las variables de historia reciente aportaran informacion predictiva incremental sobre las variables territoriales estaticas.

**H3:** el rendimiento y la calibracion variaran entre sectores; esas diferencias deberan cuantificarse antes de considerar cualquier uso institucional.

H1 y H2 son hipotesis predictivas, no causales. H3 funciona como hipotesis de heterogeneidad y criterio de seguridad.

## 4. Diseno

Estudio cuantitativo aplicado de desarrollo y validacion predictiva con observaciones repetidas por territorio y mes. El periodo propuesto es 2018-2025, condicionado por autorizacion y calidad. La fase actual es una prueba de concepto sintetica. La fase con datos reales sera retrospectiva y no intervencional.

## 5. Poblacion, unidad y criterios

- **Poblacion objetivo:** unidades territoriales de Comas observadas mensualmente.
- **Unidad de analisis:** territorio-mes.
- **Inclusion:** denuncias patrimoniales dentro de Comas, fechas validas, clasificacion armonizable y geocodificacion compatible con el nivel agregado.
- **Exclusion:** duplicados confirmados, registros fuera del periodo/ambito, coordenadas imposibles y observaciones que no puedan agregarse con seguridad.
- **Muestra:** censo de registros elegibles; se informara numero de registros, territorios, meses y eventos luego de la autorizacion. No se inventa un tamano a priori.

Se realizara un analisis de suficiencia basado en numero de eventos, prevalencia, complejidad del modelo y precision esperada de las metricas. Si los datos son insuficientes, se reducira la complejidad o se ampliara la unidad de agregacion.

## 6. Fuentes y gobierno del dato

1. Registros SIDPOL autorizados y seudonimizados antes del acceso analitico.
2. Censo Nacional 2017 del INEI, documentando el desfase temporal.
3. Cartografia oficial y, solo si existe licencia y calidad suficiente, variables municipales de infraestructura.

No se almacenaran datos personales en GitHub. La vinculacion se realizara en un entorno controlado; el repositorio publico contendra codigo, metadatos, esquemas y datos sinteticos.

## 7. Resultado y predictores

El resultado primario sera el conteo o tasa de denuncias patrimoniales en t+1. Como analisis secundario, se definiran niveles de riesgo mediante umbrales preespecificados y justificados. Todos los predictores deberan estar disponibles al cierre de t. Los rezagos se calcularan dentro de cada unidad territorial y se auditaran para evitar fuga de informacion.

## 8. Plan de analisis

1. Congelar diccionario, reglas de elegibilidad y plan analitico.
2. Evaluar duplicados, faltantes, consistencia, cobertura y error de geocodificacion.
3. Describir tasas, tendencias, estacionalidad y autocorrelacion espacial (Moran global y local cuando corresponda).
4. Entrenar baseline de prevalencia, baseline de persistencia, regresion regularizada y modelos de arboles. Modelos mas complejos solo si el volumen y la ganancia incremental los justifican.
5. Aplicar validacion temporal de ventana expansiva; reservar el periodo final como prueba intacta.
6. Aplicar validacion espacial agrupando territorios para medir transferencia a zonas no vistas.
7. Ajustar hiperparametros y umbral exclusivamente en entrenamiento/validacion.
8. Reportar PR-AUC como metrica principal de discriminacion cuando exista desbalance; ademas ROC-AUC, precision, recall, F1, Brier, curva de calibracion e intervalos bootstrap.
9. Comparar modelos con identicas particiones y reportar incertidumbre, no solo el mejor valor puntual.
10. Examinar importancia por permutacion o SHAP, estabilidad temporal y errores por sector.

## 9. Control de sesgos

Las denuncias reflejan tanto victimizacion como propension y acceso a denunciar. No se interpretaran como medicion exhaustiva del delito. Se documentaran cambios administrativos, faltantes, cobertura y posibles ciclos de realimentacion. No se usaran variables personales sensibles ni proxies sin justificacion. Las comparaciones territoriales se presentaran con tamanos de muestra e intervalos, evitando etiquetar comunidades como intrinsecamente peligrosas.

## 10. Etica y proteccion

Antes de datos reales se requeriran autorizacion institucional y evaluacion etica aplicable. El tratamiento observara la Ley N.° 29733 y normativa vigente que corresponda. Se aplicaran minimizacion, acceso por rol, cifrado, registro de accesos, agregacion, calendario de eliminacion y respuesta a incidentes. Las salidas tendran revision de revelacion y no mostraran puntos individuales.

## 11. Reproducibilidad

Codigo, parametros, semillas, versiones, hashes y decisiones analiticas se versionaran. DVC gestionara artefactos no sensibles; MLflow registrara experimentos sin incluir datos reales ni rutas reveladoras. Una reproduccion desde clon limpio debera generar las tablas principales antes del cierre del estudio.

## 12. Limitaciones

Subregistro, sesgo de denuncia, cambios de clasificacion, desfase censal, dependencia espacial, deriva temporal, calidad de geocodificacion y limitada transportabilidad fuera de Comas. El diseno predictivo no identifica causas ni demuestra que una intervencion reduzca delitos.

## 13. Productos y criterios de avance TRL

- Base analitica documentada y controlada.
- Pipeline reproducible y pruebas automatizadas.
- Informe de validacion temporal-espacial.
- Ficha del modelo, datasheet, auditoria de sesgo y protocolo etico.
- Prototipo de mapa agregado en laboratorio.

La denominacion TRL 4 se mantendra como meta y solo se afirmara como alcanzada cuando exista evidencia verificable de validacion de componentes en el entorno definido por la directiva vigente de CONCYTEC.

## 14. Cronograma resumido (24 meses)

| Fase | Meses | Producto |
|---|---:|---|
| Autorizaciones, revision y protocolo | 1-4 | Protocolo congelado y permisos. |
| Integracion y calidad de datos | 5-8 | Base y diccionario auditados. |
| Analisis y desarrollo | 9-14 | Baselines y modelos candidatos. |
| Validacion y auditorias | 15-18 | Informe temporal, espacial y de sesgos. |
| Prototipo y evaluacion | 19-21 | Mapa agregado y ficha del modelo. |
| Redaccion y transferencia | 22-24 | Tesis, articulo y paquete reproducible. |

## 15. Enmiendas

Toda modificacion posterior al congelamiento indicara fecha, motivo, impacto y si fue realizada antes o despues de observar el conjunto de prueba. Los analisis no preespecificados se rotularan como exploratorios.
