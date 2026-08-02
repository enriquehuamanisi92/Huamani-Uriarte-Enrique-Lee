# Auditoria de reproducibilidad

## Alcance

Auditoria del artefacto sintetico actual. No certifica la futura fase con SIDPOL.

| Componente | Estado | Evidencia / accion pendiente |
|---|---|---|
| Codigo de generacion | Cumple | `05_pipeline/data/create_dataset.py`, semilla fija. |
| Separacion temporal | Parcial | Existe holdout por ano; falta ventana rodante y prueba espacial. |
| Prevencion de fuga | Parcial | Los rezagos sinteticos usan `shift`; faltan tests automatizados. |
| Dependencias | Parcial | Existe `requirements.txt`; deben fijarse versiones y Python. |
| Datos | Cumple para demo | CSV sintetico y script; los datos reales nunca iran al repositorio publico. |
| Registro de experimentos | Parcial | MLflow existe, pero se versionaron demasiados archivos de ejecucion. |
| Resultados | Cumple para demo | CSV consolidado; debe incluir media, dispersion e intervalos. |
| Notebook | Parcial | Sin salidas guardadas; verificar ejecucion limpia. |
| Contenedor | Parcial | Dockerfile presente; falta prueba automatizada de construccion. |
| Integridad de artefactos | Pendiente | Registrar SHA-256 de datos, configuracion y commit. |
| Reproduccion independiente | Pendiente | Una segunda persona debe clonar y registrar resultado real. |

## Prueba de clon limpio

1. Clonar una version etiquetada.
2. Crear ambiente con la version documentada de Python.
3. Instalar dependencias sin modificaciones manuales.
4. Regenerar el CSV sintetico.
5. Ejecutar experimentos y comparar filas, modelos y tolerancia de metricas.
6. Registrar sistema operativo, Python, tiempo, commit y diferencias.

## Hallazgo principal

Los valores actuales demuestran que el software procesa datos sinteticos. No prueban validez externa. Antes de una entrega final deben excluirse nuevas carpetas `mlruns/` de Git, conservar un resumen curado y gestionar artefactos extensos mediante DVC o almacenamiento institucional.
