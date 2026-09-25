# Taller 2 · Listas de espera: ¿cómo varían por provincia y especialidad?

## Guía del profesorado

### Ubicación curricular
Módulos de Gestión de Pacientes, Organización y Gestión de Servicios de Salud, o Documentación Sanitaria, en ciclos de Grado Superior de Sanidad (Documentación y Administración Sanitarias). Refuerza resultados de aprendizaje sobre "gestión de flujos de pacientes" y "análisis de indicadores de actividad asistencial" habituales en estos currículos.

### Duración
3 sesiones de 55 minutos.

### Requisitos previos del alumnado
Haber trabajado previamente el concepto de agregación de datos (Taller 1) o, si se imparte de forma independiente, dedicar 10 minutos iniciales a repasar `groupby`/tablas dinámicas con un ejemplo sencillo no sanitario.

### Materiales necesarios
- Dataset de lista de espera quirúrgica descargado previamente por el profesorado como copia de seguridad.
- Excel/LibreOffice Calc con tablas dinámicas, o Jupyter Notebook/Google Colab con `pandas`.
- Acceso a los informes del SISNS (Ministerio de Sanidad) para la Actividad 4, o el dato de referencia proporcionado por el profesorado si no hay acceso a internet en el aula.

### Secuencia didáctica sugerida

**Sesión 1 (55 min):**
- 15 min: introducción al concepto de lista de espera y su relevancia en la gestión sanitaria pública, con ejemplo de un caso real anonimizado o hipotético.
- 40 min: Actividades 1 y 2.

**Sesión 2 (55 min):**
- Actividad 3 completa, con atención especial a que el alumnado interprete correctamente gráficos de barras agrupadas (es habitual que el alumnado confunda el eje de agrupación).

**Sesión 3 (55 min):**
- Actividad 4 y discusión final.
- 15 min: debate guiado sobre equidad territorial en el acceso a la sanidad, especialmente relevante en Castilla y León por su dispersión poblacional.
- Recogida del entregable.

### Orientaciones metodológicas
- Es un buen momento para introducir el concepto de "brecha rural-urbana" en el acceso a servicios sanitarios especializados.
- Si el centro está en una provincia concreta, se recomienda que la Actividad 3 se centre también en esa provincia, para dar mayor cercanía y motivación al ejercicio.
- Adaptación DUA: el alumnado con más dificultad puede trabajar con una tabla ya agregada (proporcionada por el profesorado) centrándose solo en la construcción del gráfico e interpretación; el alumnado más avanzado puede ampliar el análisis a más de 3 especialidades o añadir un cálculo de percentiles en lugar de solo la media.

### Solución orientativa (para contraste, no para entregar al alumnado)
Las especialidades quirúrgicas con mayores tiempos de espera suelen ser traumatología, oftalmología (especialmente cirugía de cataratas) y cirugía general, con variabilidad relevante entre provincias, tendiendo a ser mayor en las provincias con menor densidad de especialistas. Los valores concretos dependen del periodo consultado en el dataset; se recomienda que el profesorado ejecute el notebook con antelación para disponer de las cifras exactas de la sesión.

### Errores frecuentes del alumnado y cómo abordarlos
- Comparar el número absoluto de pacientes en espera entre provincias sin tener en cuenta el tamaño de población: recordar que hay que fijarse también en el tiempo medio de espera, no solo en el volumen.
- Malinterpretar gráficos de barras agrupadas: reforzar la lectura del eje X (categoría principal) frente a la leyenda (subcategoría).
- Extraer conclusiones simplistas sobre "mala gestión" sin considerar otros factores (envejecimiento poblacional, dispersión geográfica, disponibilidad de especialistas): fomentar el pensamiento crítico y la búsqueda de más de una causa posible.

### Criterios de evaluación
Ver rúbrica de evaluación común en `rubricas/rubricas_evaluacion.md`, apartado Taller 2. Ponderación orientativa: 25% comprensión del dataset, 45% análisis y visualización, 30% interpretación y reflexión.
