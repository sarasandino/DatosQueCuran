# Taller 1 · Análisis de coberturas de vacunación en Castilla y León

## Guía del alumnado

### Resultados de aprendizaje
Al finalizar este taller serás capaz de:
1. Explicar qué es una cobertura de vacunación y por qué es un indicador clave en salud pública.
2. Localizar, descargar e interpretar un conjunto de datos abierto del Portal de Datos Abiertos de la Junta de Castilla y León.
3. Aplicar comprobaciones básicas de calidad de datos (valores nulos, rangos, duplicados).
4. Construir e interpretar visualizaciones de evolución temporal y comparación territorial.
5. Argumentar, con base en datos, posibles causas de desigualdad en cobertura vacunal entre provincias.

### Por qué importa esto en tu profesión
Si trabajas en un centro de salud, en farmacia o en gestión sanitaria, te vas a encontrar indicadores de cobertura constantemente: en campañas de vacunación infantil, en la vacunación de gripe de personas mayores, o en alertas de brotes. Cuando la cobertura de una vacuna cae por debajo del **95%** en una población, se pierde la llamada "inmunidad de grupo": aunque una persona esté vacunada, puede estar en riesgo si las personas de su entorno no lo están. Este taller te enseña a leer ese dato con criterio, no solo a mirarlo.

### Dataset de trabajo
**Coberturas de vacunación en Castilla y León**
- Fuente: Portal de Datos Abiertos de la Junta de Castilla y León.
- Acceso: portal de análisis de datos abiertos, dataset con identificador `coberturas-de-vacunacion-en-castilla-y-leon` (analisis.datosabiertos.jcyl.es).
- Contenido: dosis y porcentaje de cobertura de vacunas del calendario infantil (hexavalente, DTPa, Hib, VPI, entre otras) por provincia, año y grupo de edad.
- Formato: descargable en CSV.

### Antes de empezar: vocabulario clave
- **Cobertura vacunal**: porcentaje de la población objetivo que ha recibido una vacuna concreta.
- **Inmunidad de grupo**: protección indirecta que se produce cuando un porcentaje suficientemente alto de la población está inmunizado.
- **Serie temporal**: conjunto de datos ordenados en el tiempo (por ejemplo, cobertura año a año).
- **Valor nulo/perdido**: un dato ausente en el conjunto, que hay que detectar antes de calcular cualquier media o porcentaje.

### Actividades

**Actividad 1 — Primer contacto con el dataset (25 min)**
1. Descarga el dataset en formato CSV desde el portal.
2. Ábrelo en Excel o cárgalo en el notebook de Python (sección "Celda 2" del notebook de este taller).
3. Completa esta tabla en tu cuaderno de trabajo:

| Pregunta | Tu respuesta |
|---|---|
| ¿Cuántas filas tiene el dataset? | |
| ¿Qué provincias aparecen? | |
| ¿Qué vacunas se recogen? | |
| ¿Qué rango de años cubre? | |

**Actividad 2 — Control de calidad del dato (30 min)**
Antes de analizar cualquier dato sanitario, hay que verificar que es fiable. Realiza estas tres comprobaciones:
1. ¿Hay valores vacíos (nulos) en la columna de cobertura? ¿En qué filas?
2. ¿Todos los porcentajes de cobertura están entre 0% y 100%? Un valor fuera de ese rango indicaría un error de registro.
3. ¿Los nombres de provincia están escritos siempre igual (por ejemplo, "León" y no "Leon" o "LEÓN" mezclados)? Si no, corrígelo.

*Checkpoint: si tu limpieza es correcta, el número de filas útiles debería mantenerse igual o reducirse solo ligeramente respecto al total original. Si se reduce mucho, revisa qué filtro has aplicado.*

**Actividad 3 — Evolución temporal de una vacuna (45 min)**
1. Elige una vacuna del calendario infantil (por ejemplo, la vacuna hexavalente).
2. Calcula la cobertura media anual en el conjunto de Castilla y León.
3. Construye un gráfico de líneas: años en el eje X, cobertura (%) en el eje Y.
4. Redacta 3-4 líneas describiendo la tendencia: ¿sube, baja, se mantiene? ¿Hay algún año con un cambio brusco? ¿Se te ocurre alguna causa (por ejemplo, la pandemia de COVID-19 en 2020-2021 afectó a muchos programas de vacunación infantil en España)?

**Actividad 4 — Comparativa entre provincias (45 min)**
1. Para el último año disponible en el dataset, calcula la cobertura de la misma vacuna en cada provincia de Castilla y León.
2. Construye un gráfico de barras ordenado de mayor a menor cobertura, marcando el umbral del 95%.
3. Identifica las provincias por debajo del umbral y las que están más por encima.
4. Reflexiona: ¿qué factores podrían explicar diferencias entre provincias (dispersión rural, accesibilidad a centros de salud, tamaño de la población, campañas locales)?

### Preguntas de reflexión final
- ¿Por qué es relevante que estos datos sean públicos y de libre acceso, en lugar de estar solo en manos de la administración sanitaria?
- Si trabajaras en atención primaria, ¿cómo usarías un panel como este para priorizar una campaña de vacunación?
- ¿Qué limitaciones tiene este dataset? (por ejemplo: no distingue entre vacunación pública y privada, no incluye motivos de no vacunación, etc.)

### Entregable
Un documento (PDF, Word o notebook exportado) de 1-2 páginas que incluya: la tabla de la Actividad 1, los dos gráficos de las Actividades 3 y 4, y tus respuestas redactadas a las preguntas de reflexión. Se evaluará con la rúbrica común (ver `rubricas/rubricas_evaluacion.md`).
