# Taller 3 · Farmacia y medicamentos: análisis de dispensaciones

## Guía del profesorado

### Ubicación curricular
Módulos de Dispensación de Productos Farmacéuticos y Parafarmacéuticos, Oficina de Farmacia, o Farmacotecnia, dentro del ciclo de Técnico en Farmacia y Parafarmacia. También aplicable a módulos de estadística sanitaria o TIC aplicadas a la salud en otros ciclos de la familia de Sanidad.

### Duración
2 sesiones de 55 minutos.

### Requisitos previos del alumnado
Manejo básico de agrupación de datos por categorías (reforzado en los Talleres 1 y 2). Si se imparte de forma aislada, dedicar 10 minutos iniciales a repasar `groupby`/tabla dinámica con un ejemplo sencillo.

### Materiales necesarios
- Dataset de consumo de productos farmacéuticos por receta, descargado previamente por el profesorado.
- Excel/LibreOffice Calc, o Jupyter Notebook/Google Colab con `pandas` y `matplotlib`.

### Secuencia didáctica sugerida

**Sesión 1 (55 min):**
- 15 min: introducción al ciclo de dispensación de medicamentos con receta en el sistema público y a la fuente de datos utilizada.
- 40 min: Actividades 1, 2 y 3.

**Sesión 2 (55 min):**
- Actividad 4 sobre patrones estacionales.
- 15 min finales: puesta en común y conexión explícita con contenidos de Farmacología (estacionalidad de patologías respiratorias y alérgicas).

### Orientaciones metodológicas
- Es el taller idóneo para conectar con contenidos de Farmacología sobre estacionalidad de determinadas patologías.
- Como ampliación, se puede proponer comparar los datos de consumo de medicamentos respiratorios con los datos de vacunación de gripe trabajados en el Taller 1, si el grupo ya lo ha realizado, para reforzar la idea de que distintos datasets sanitarios están interrelacionados.
- Adaptación DUA: el alumnado con más dificultad puede centrarse solo en un tipo de producto (por ejemplo, el más consumido) para las Actividades 3 y 4; el alumnado más avanzado puede comparar la estacionalidad de dos o tres tipos de producto distintos en el mismo gráfico.

### Solución orientativa (para contraste, no para entregar al alumnado)
El consumo de medicamentos respiratorios y antigripales suele mostrar un pico en los meses de invierno (noviembre a febrero), mientras que los antihistamínicos muestran habitualmente un repunte en primavera, coincidiendo con la temporada de polinización. Los valores exactos dependen del periodo y tipo de producto consultado en el dataset; se recomienda que el profesorado ejecute el notebook con antelación para disponer de cifras concretas.

### Errores frecuentes del alumnado y cómo abordarlos
- Confundir "número de envases" con "número de pacientes": un mismo paciente puede recibir varios envases del mismo medicamento en un periodo.
- No tener en cuenta que los datos agregan varios años: si no se agrupa correctamente por mes (ignorando el año), la serie estacional puede salir distorsionada por la tendencia general de varios años.
- Extraer conclusiones sin verificar que el tipo de producto elegido realmente tiene un patrón estacional esperado: guiar al alumnado a elegir productos con lógica clínica clara (respiratorios, antihistamínicos) antes de generalizar a otros.

### Criterios de evaluación
Ver rúbrica de evaluación común en `rubricas/rubricas_evaluacion.md`, apartado Taller 3. Ponderación orientativa: 25% comprensión del dataset, 45% análisis y visualización, 30% interpretación y reflexión.
