# Taller 2 · Listas de espera: ¿cómo varían por provincia y especialidad?

## Guía del alumnado

### Resultados de aprendizaje
Al finalizar este taller serás capaz de:
1. Explicar qué es una lista de espera quirúrgica y qué información aporta a la gestión sanitaria.
2. Agregar datos por categorías (especialidad, provincia) y calcular medidas de tendencia central.
3. Construir visualizaciones comparativas y detectar desigualdades territoriales en el acceso a la sanidad.
4. Contrastar datos autonómicos con datos de referencia nacional.

### Por qué importa esto en tu profesión
Si trabajas en gestión de pacientes, documentación sanitaria o administración de centros de salud, la lista de espera es una de las métricas que más se revisa a nivel de dirección. Detrás de cada día de espera hay un paciente cuya calidad de vida se ve afectada. Aprender a leer estos datos con rigor te permite entender por qué unas especialidades o zonas tardan más que otras, y qué margen de mejora hay.

### Dataset de trabajo
**Lista de espera quirúrgica**
- Fuente: Catálogo de Información Pública, Consejería de Sanidad, Junta de Castilla y León (con compromiso de publicidad periódica).
- Contenido: número de pacientes en espera y tiempo medio de espera (en días), desglosado por especialidad y provincia, con datos habitualmente referidos a 31 de diciembre.
- Formato: descargable en CSV/XLS.

### Antes de empezar: vocabulario clave
- **Paciente en espera estructural**: paciente que en un momento dado está pendiente de ser intervenido, dentro de los tiempos de garantía establecidos.
- **Tiempo medio de espera**: número de días que, en promedio, tarda un paciente en ser intervenido desde que se indica la cirugía.
- **Especialidad quirúrgica**: área médica a la que pertenece la intervención (traumatología, oftalmología, cirugía general, etc.).

### Actividades

**Actividad 1 — Estructura del dataset (20 min)**
1. Descarga el archivo CSV/XLS del dataset de lista de espera quirúrgica.
2. Identifica las columnas disponibles: provincia, especialidad, número de pacientes en espera, tiempo medio de espera.
3. Anota cuántas especialidades distintas aparecen en el dataset.

**Actividad 2 — Tiempo medio de espera por especialidad (40 min)**
1. Calcula el tiempo medio de espera de cada especialidad en el conjunto de Castilla y León.
2. Ordena las especialidades de mayor a menor tiempo de espera.
3. Construye un gráfico de barras horizontales con el resultado.
4. Identifica las 3 especialidades con mayor tiempo de espera.

**Actividad 3 — Comparativa por provincia (40 min)**
1. Para las 3 especialidades con mayor tiempo de espera (obtenidas en la Actividad 2), calcula el tiempo medio de espera en cada provincia.
2. Construye un gráfico de barras agrupadas (una barra por especialidad, agrupadas por provincia).
3. Identifica la provincia con mayor y menor tiempo de espera para cada una de esas especialidades.

**Actividad 4 — Comparación con la media nacional (30 min)**
1. Localiza un dato de referencia de tiempo medio de espera quirúrgica a nivel nacional (por ejemplo, en los informes del Sistema de Información del Sistema Nacional de Salud, SISNS, del Ministerio de Sanidad).
2. Compara la media de Castilla y León con esa referencia nacional.
3. Redacta una conclusión: ¿Castilla y León está por encima o por debajo? ¿En qué especialidades la diferencia es mayor?

### Preguntas de reflexión final
- ¿Qué factores estructurales pueden influir en que una especialidad tenga listas de espera más largas que otra (número de especialistas, quirófanos disponibles, complejidad de la intervención)?
- ¿Cómo podría un gestor sanitario usar estos datos para decidir dónde reforzar recursos?
- Piensa en un paciente concreto (por ejemplo, alguien que espera una intervención de cadera): ¿qué impacto tiene un tiempo de espera largo en su vida diaria?

### Entregable
Documento con los dos gráficos comparativos de las Actividades 2 y 3, la conclusión de la Actividad 4, y las respuestas redactadas a las preguntas de reflexión.
