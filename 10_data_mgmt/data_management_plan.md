# Plan de gestion de datos de investigacion

## 1. Tipos de datos

| Categoria | Ejemplo | Clasificacion | Repositorio permitido |
|---|---|---|---|
| Publico sintetico | CSV generado y resultados demostrativos. | Publico, rotulado sintetico. | Git/DVC. |
| Publico oficial | Cartografia o tablas abiertas con licencia. | Segun licencia. | Git/DVC o almacenamiento institucional. |
| Restringido fuente | Registros SIDPOL autorizados. | Confidencial/sensible. | Entorno institucional controlado. |
| Derivado restringido | Datos geocodificados o celdas pequenas. | Confidencial mientras exista revelacion. | Entorno institucional controlado. |
| Derivado publicable | Estadisticas agregadas aprobadas. | Publico tras revision. | Repositorio institucional/Git. |

## 2. Responsabilidades

El custodio institucional conserva autoridad sobre los datos fuente. El investigador principal asegura cumplimiento del protocolo, accesos, versionado y reporte. Los colaboradores reciben solo el acceso indispensable y aceptan por escrito finalidad, confidencialidad y procedimiento de incidentes.

## 3. Ciclo de vida

1. **Adquisicion:** registrar fuente, autorizacion, fecha, licencia y hash.
2. **Ingesta:** validar esquema en zona aislada; no sobrescribir originales.
3. **Procesamiento:** scripts versionados crean capas intermedias y analiticas.
4. **Analisis:** ambiente controlado, parametros y semillas registrados.
5. **Revision:** comprobar calidad, revelacion y coherencia antes de exportar.
6. **Preservacion:** conservar codigo, metadatos y productos permitidos.
7. **Eliminacion:** ejecutar y documentar la politica acordada con el custodio.

## 4. Convenciones y metadatos

Fechas ISO 8601; UTF-8; identificadores estables no semanticos; sistema de coordenadas declarado; diccionario con nombre, tipo, unidad, fuente, transformacion, faltantes y sensibilidad. Cada version analitica tendra hash, commit, fecha y responsable.

## 5. Calidad

Controles de esquema, rango, unicidad, duplicados, faltantes, consistencia temporal, pertenencia espacial, tasas de geocodificacion y cambios de clasificacion. Toda correccion sera scriptada; los cambios manuales requeriran bitacora.

## 6. FAIR con limites

Se maximizaran encontrabilidad, accesibilidad controlada, interoperabilidad y reutilizacion del codigo y metadatos. FAIR no significa datos abiertos: los microdatos sensibles permaneceran restringidos. Se publicaran datos sinteticos, diccionarios y, cuando sea seguro y autorizado, estadisticas agregadas.

## 7. Respaldo y continuidad

Copias cifradas y versionadas segun politica institucional, prueba periodica de restauracion y separacion entre respaldo y ambiente de trabajo. Git no es respaldo autorizado de datos reales.

## 8. Retencion

La duracion concreta se fijara en el convenio y aprobacion etica. Al cierre se eliminan copias de trabajo, credenciales y llaves no necesarias; se conserva evidencia no sensible para auditoria conforme a las reglas institucionales.
