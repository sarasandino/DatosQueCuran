# Taller 3 · Farmacia y medicamentos: análisis de dispensaciones

## Guía del alumnado

### Resultados de aprendizaje
Al finalizar este taller serás capaz de:
1. Explicar cómo se registra el consumo de medicamentos dispensados con receta en el sistema sanitario público.
2. Agrupar y comparar datos de consumo por tipo de producto y provincia.
3. Identificar patrones estacionales en series temporales mensuales.
4. Relacionar patrones de consumo farmacéutico con fenómenos sanitarios conocidos (por ejemplo, la estacionalidad de la gripe).

### Por qué importa esto en tu profesión
Si trabajas o vas a trabajar en una oficina de farmacia o en el área de dispensación de un centro sanitario, entender los patrones de consumo te ayuda a anticipar necesidades de stock, detectar tendencias de salud pública y comprender mejor el ciclo de vida de un medicamento desde su prescripción hasta su dispensación. Este taller usa datos reales de dispensación con receta en Castilla y León.

### Dataset de trabajo
**Consumo de productos farmacéuticos por receta**
- Fuente: Portal de Datos Abiertos de la Junta de Castilla y León.
- Acceso: portal de análisis de datos abiertos, dataset con identificador `consumo-de-productos-farmaceuticos-por-receta` (analisis.datosabiertos.jcyl.es).
- Contenido: número de envases consumidos e importe, desglosado por tipo de producto (medicamentos, efectos y accesorios, dietoterápicos/dietéticos, fórmulas magistrales), mes y provincia.
- Formato: descargable en CSV.

### Antes de empezar: vocabulario clave
- **Envase dispensado**: unidad de medicamento entregada al paciente en la farmacia con cargo a receta del sistema público.
- **PVP (Precio de Venta al Público)**: precio final del medicamento antes de aplicar aportaciones o descuentos.
- **Estacionalidad**: patrón que se repite en determinados periodos del año (por ejemplo, más consumo de antigripales en invierno).

### Actividades

**Actividad 1 — Estructura del dataset (20 min)**
1. Descarga el dataset en CSV.
2. Identifica las columnas: mes, provincia, tipo de producto, número de envases, importe.
3. Anota cuántos tipos de producto distintos aparecen.

**Actividad 2 — Control de calidad de los datos (20 min)**
1. Comprueba que no haya meses o provincias con nombres duplicados por errores de escritura.
2. Verifica que la columna de fecha/mes tiene un formato reconocible (por ejemplo, AAAA-MM).
3. Comprueba que no haya valores negativos en número de envases o importe (no tendría sentido clínico ni contable).

**Actividad 3 — Consumo por tipo de producto y provincia (40 min)**
1. Calcula el número total de envases consumidos por tipo de producto en todo el periodo disponible.
2. Construye un gráfico de barras con el resultado.
3. Para el tipo de producto más consumido, calcula el desglose por provincia y represéntalo también en un gráfico.

**Actividad 4 — Patrones estacionales (40 min)**
1. Elige un tipo de producto con posible componente estacional (por ejemplo, medicamentos respiratorios o antihistamínicos).
2. Suma el número de envases consumidos por mes (agrupando todos los años disponibles en el dataset).
3. Construye un gráfico de líneas con los 12 meses en el eje X.
4. Redacta una conclusión: ¿se observa un patrón estacional claro? ¿En qué meses hay más consumo? ¿Coincide con lo que sabes sobre la estacionalidad de esa patología?

### Preguntas de reflexión final
- ¿Por qué es útil para una farmacia o un gestor sanitario anticipar estos patrones estacionales?
- ¿Qué relación podría existir entre el consumo de medicamentos respiratorios y los datos de vacunación de gripe (si has hecho el Taller 1, compáralo)?
- ¿Qué limitaciones tiene este dataset para conocer el consumo real de medicamentos en la población? (Piensa, por ejemplo, en los medicamentos sin receta o los adquiridos fuera del sistema público.)

### Entregable
Documento con los gráficos de las Actividades 3 y 4, la tabla resumen por tipo de producto y provincia, y las respuestas redactadas a las preguntas de reflexión.
