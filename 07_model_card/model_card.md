# Ficha del modelo — prototipo sintetico

## Identificacion

- **Nombre:** Comas Urban Crime Risk Prototype.
- **Version:** 0.1-synthetic.
- **Responsable:** Enrique Lee Huamani Uriarte.
- **Estado:** prueba de concepto; no desplegable.

## Proposito previsto

Demostrar un pipeline reproducible para estimar riesgo agregado del mes siguiente por unidad territorial. En una fase autorizada podria apoyar analisis preventivo y priorizacion de diagnosticos con supervision humana.

## Usos prohibidos

- Identificar, puntuar, vigilar o detener personas.
- Inferir culpabilidad, reincidencia o pertenencia a grupos.
- Asignar automaticamente patrullaje, sanciones o recursos.
- Publicar direcciones, coordenadas puntuales o mapas que faciliten reidentificacion.
- Utilizar las metricas sinteticas como evidencia de eficacia real.

## Datos y resultado actual

Datos totalmente sinteticos de 64 zonas mensuales entre 2018-2025. La etiqueta binaria representa que el conteo sintetico del mes siguiente supera un percentil global. Esa definicion es didactica y no es una definicion institucional de riesgo.

## Evaluacion actual

Se reportan ROC-AUC, PR-AUC, exactitud, precision, recall y F1 en un holdout temporal desde 2024. Random Forest alcanza alrededor de 0.84 ROC-AUC en los experimentos guardados. El resultado es esperado porque datos y etiqueta provienen de reglas simuladas. Falta calibracion, baseline de persistencia, intervalos, validacion rodante y espacial.

## Riesgos

Subregistro, sesgo de denuncia, realimentacion policial, deriva, geocodificacion desigual, estigmatizacion territorial, proxies sensibles y falsa confianza en puntajes. Un mapa puede causar dano aun sin identificar personas.

## Requisitos antes de cambiar el estado

Permisos y etica; datos agregados; prueba independiente; comparadores; calibracion; auditoria de disparidades; documentacion de incertidumbre; aprobacion humana; monitoreo y procedimiento de retiro. Hasta entonces el estado es **NO APTO PARA USO OPERATIVO**.
