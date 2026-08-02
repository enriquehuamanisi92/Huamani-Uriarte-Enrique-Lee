# Prediccion del riesgo delictivo urbano en Comas

**Autor:** Enrique Lee Huamani Uriarte

**Curso:** Metodos de investigacion e integridad cientifica en inteligencia artificial y tecnologias avanzadas, UNMSM

**Estado:** protocolo de investigacion y prueba de concepto con datos sinteticos

## Proyecto en un parrafo

Esta investigacion propone desarrollar y validar un modelo de aprendizaje automatico y analisis geoespacial que estime, para cada unidad territorial de Comas y cada mes, el riesgo de delitos patrimoniales del periodo siguiente. El estudio integrara denuncias policiales autorizadas, variables censales y caracteristicas territoriales. Su producto esperado es un prototipo TRL 4 para apoyo a la gestion preventiva; no identifica personas, no predice autores y no autoriza decisiones policiales automaticas. El pipeline actual usa exclusivamente datos sinteticos y demuestra reproducibilidad informatica, no eficacia en condiciones reales.

## Pregunta y objetivo general

**Pregunta:** ¿En que medida un modelo de aprendizaje automatico que integra antecedentes delictivos, variables socioeconomicas y caracteristicas geoespaciales predice el riesgo mensual de delitos patrimoniales en unidades territoriales de Comas, en comparacion con baselines historicos, bajo validacion temporal y espacial?

**Objetivo:** desarrollar y validar dicho modelo, evaluar su discriminacion, calibracion, utilidad y estabilidad territorial, e implementar salvaguardas de privacidad, equidad, explicabilidad y supervision humana.

## Mapa del repositorio

| Carpeta | Contenido |
|---|---|
| `01_paradigm/` | Paradigma, alcance y posicion epistemologica. |
| `02_method/` | Comparacion de metodos y matriz de consistencia. |
| `03_protocol/` | Esquema inicial y protocolo completo v1.0. |
| `04_literature/` | Revision exploratoria, protocolo de busqueda y brechas. |
| `05_pipeline/` | Datos sinteticos, codigo, notebook y resultados tecnicos. |
| `06_repro_audit/` | Auditoria y lista de verificacion de reproducibilidad. |
| `07_model_card/` | Ficha del modelo y ficha del conjunto de datos. |
| `09_ethics/` | Protocolo etico y limites de uso. |
| `10_data_mgmt/` | Plan de gestion de datos. |
| `11_bias_audit/` | Plan de evaluacion de sesgos y desempeno por subgrupos. |
| `12_integrity/` | Politica de uso de IA e integridad cientifica. |

## Estado de la evidencia

- **Completado:** formulacion metodologica, protocolo v1.0, documentos de gobernanza y pipeline sintetico reproducible.
- **Preliminar:** revision exploratoria de literatura; sus conteos PRISMA anteriores no deben considerarse resultados definitivos hasta ejecutar y exportar las busquedas.
- **Pendiente:** autorizacion y acceso a datos reales, protocolo de geocodificacion, revision por comite de etica, busqueda sistematica auditada y validacion externa.

## Reproduccion de la prueba de concepto

```bash
cd 05_pipeline
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python data/create_dataset.py
python src/run_experiments.py
```

Los resultados sinteticos no deben citarse como evidencia sobre seguridad ciudadana en Comas. Consulte `05_pipeline/README.md` para las rutas local, Docker y Colab.

## Uso responsable

No se deben subir a GitHub registros SIDPOL, direcciones, coordenadas puntuales, datos de victimas, denunciantes o personas investigadas. Las salidas publicas seran agregadas y sujetas a control de revelacion. Cualquier uso institucional requerira autorizacion, evaluacion etica, validacion con datos reales, auditoria de sesgos y decision humana documentada.

## Fuentes normativas y metodologicas clave

- Congreso de la Republica del Peru. Ley N.° 29733, Ley de Proteccion de Datos Personales.
- CONCYTEC. Directiva N.° 001-2022-CONCYTEC-P para el uso de niveles de madurez tecnologica.
- Page et al. (2021). PRISMA 2020 statement. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71
