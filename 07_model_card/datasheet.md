# Ficha del conjunto de datos sintetico

## Motivacion y composicion

El archivo `comas_urban_crime_synthetic.csv` sirve para probar codigo sin exponer informacion real. Contiene observaciones zona-mes simuladas, coordenadas aproximadas, atributos territoriales ficticios, rezagos de incidentes y una etiqueta futura derivada.

No contiene SIDPOL, denuncias reales, victimas, investigados, direcciones ni datos municipales operativos. Los nombres de sectores dan contexto pedagogico, pero sus valores no describen dichos sectores.

## Generacion y trazabilidad

Se genera con `create_dataset.py`, NumPy y semilla 42. Las relaciones fueron programadas expresamente; por tanto, no pueden usarse para inferir asociaciones sociales reales. El CSV puede regenerarse y su puntero DVC permite verificar la version.

## Limitaciones y uso

- No representa distribuciones, fronteras ni prevalencia real de Comas.
- No permite validar equidad sustantiva ni utilidad institucional.
- No debe combinarse con datos personales ni presentarse como estadistica oficial.
- Es adecuado para pruebas de ejecucion, estructura, versionado y demostracion en clase.

## Futuro conjunto real

Tendra una ficha separada y restringida con procedencia, base legal, custodio, variables, licencias, cobertura, faltantes, geocodificacion, transformaciones, controles, acceso, retencion y evaluacion de revelacion. Nunca se reemplazara silenciosamente esta ficha sintetica.
