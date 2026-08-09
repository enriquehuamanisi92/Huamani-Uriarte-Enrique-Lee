# Hoja de trabajo para el diagrama PRISMA 2020

Esta hoja corresponde al formato «PRISMA 2020 flow diagram for new systematic reviews» proporcionado para la presentación. Sustituya `PENDIENTE` únicamente con conteos obtenidos de las exportaciones y bitácoras.

## 1. Identificación

| Campo del formato | Valor | Fuente de verificación |
|---|---:|---|
| Registros identificados en Scopus | PENDIENTE | Exportación y `search_log.csv` |
| Registros identificados en Web of Science | PENDIENTE | Exportación y `search_log.csv` |
| Registros identificados en IEEE Xplore | PENDIENTE | Exportación y `search_log.csv` |
| Registros identificados en ACM Digital Library | PENDIENTE | Exportación y `search_log.csv` |
| Registros identificados en SciELO | PENDIENTE | Exportación y `search_log.csv` |
| Registros identificados en registros | 0, salvo que se use uno | Exportación |
| **Total identificado** | **PENDIENTE** | Suma de las filas anteriores |

## 2. Eliminación antes del cribado

| Campo del formato | Valor | Fuente de verificación |
|---|---:|---|
| Duplicados eliminados | PENDIENTE | Registro de deduplicación |
| Marcados como inelegibles por automatización | 0, salvo uso documentado | Log de la herramienta |
| Eliminados por otras razones | PENDIENTE | Motivo documentado |
| **Registros que pasan a cribado** | **PENDIENTE** | Total identificado menos eliminaciones |

## 3. Cribado y recuperación

| Campo del formato | Valor | Fuente de verificación |
|---|---:|---|
| Registros cribados por título/resumen | PENDIENTE | `screening_log.csv` |
| Registros excluidos | PENDIENTE | `screening_log.csv` |
| Informes buscados para recuperación | PENDIENTE | Diferencia de las dos filas anteriores |
| Informes no recuperados | PENDIENTE | Intentos documentados |
| Informes evaluados para elegibilidad | PENDIENTE | `screening_log.csv` |

## 4. Exclusiones a texto completo

Use razones mutuamente excluyentes y conserve una razón principal por informe.

| Razón | n |
|---|---:|
| Sin predicción fuera de muestra | PENDIENTE |
| Predicción individual fuera del alcance | PENDIENTE |
| Contexto no urbano o no transferible | PENDIENTE |
| Datos/método insuficientemente descritos | PENDIENTE |
| Tipo documental no elegible | PENDIENTE |
| Duplicado no detectado previamente | PENDIENTE |
| Otra razón especificada | PENDIENTE |
| **Total de informes excluidos** | **PENDIENTE** |

## 5. Inclusión

| Campo del formato | Valor | Fuente de verificación |
|---|---:|---|
| Estudios incluidos en la revisión | PENDIENTE | Identificadores únicos de estudio |
| Informes de los estudios incluidos | PENDIENTE | Documentos asociados |

Un estudio puede tener más de un informe; por ello ambas cifras pueden diferir.

## 6. Controles antes de completar el Word

1. Registros cribados = total identificado − duplicados − automatización − otras eliminaciones previas.
2. Informes buscados = registros cribados − registros excluidos.
3. Informes evaluados = informes buscados − informes no recuperados.
4. Informes evaluados = informes excluidos a texto completo + informes incluidos.
5. Cada número debe poder reconstruirse desde `search_log.csv` o `screening_log.csv`.
6. Si no se utilizaron herramientas de automatización, registre cero; no deje el campo ambiguo.
7. Reporte, cuando sea posible, el número identificado por cada base, como recomienda la nota del formato PRISMA.
