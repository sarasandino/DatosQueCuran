# Taller 1 · Análisis de coberturas de vacunación en Castilla y León

## Guía del profesorado

### Ubicación curricular
Módulos de Promoción de la Salud, Educación para la Salud, Salud Pública, o Documentación Sanitaria, en ciclos de Grado Medio/Superior de la familia profesional de Sanidad. Conecta directamente con resultados de aprendizaje relativos a "identificar indicadores de salud y su aplicación en programas de prevención" presentes en los currículos de varios ciclos (CAE, Farmacia, Documentación Sanitaria).

### Duración
3 sesiones de 55 minutos (150 minutos totales aproximados, incluyendo puesta en común).

### Resultados de aprendizaje curriculares que se refuerzan
- Interpretación de indicadores de salud pública a partir de fuentes de datos oficiales.
- Manejo de herramientas ofimáticas o de programación para el tratamiento de datos.
- Comunicación oral y escrita de resultados con base empírica.

### Requisitos previos del alumnado
- **Nivel Básico (Excel)**: manejo de filtros, tablas y gráficos sencillos. No requiere conocimientos previos de programación.
- **Nivel Avanzado (Python)**: no se requiere experiencia previa; el notebook está comentado línea a línea y pensado para ejecutarse guiado por el profesorado la primera vez.

### Materiales necesarios
- Ordenadores con acceso a internet, o el CSV descargado previamente por el profesorado como copia de seguridad (los portales de datos abiertos pueden tener mantenimientos puntuales).
- Excel/LibreOffice Calc, o bien Jupyter Notebook/Google Colab con Python 3.
- Proyector para las puestas en común.

### Secuencia didáctica sugerida

**Sesión 1 (55 min):**
- 10 min: introducción al concepto de cobertura vacunal e inmunidad de grupo, apoyada en un ejemplo real reciente (por ejemplo, brotes de sarampión en Europa en años con baja cobertura).
- 20 min: Actividad 1 (primer contacto con el dataset), en parejas.
- 20 min: Actividad 2 (control de calidad), con puesta en común de errores encontrados.
- 5 min: cierre y adelanto de la siguiente sesión.

**Sesión 2 (55 min):**
- Actividad 3 completa (evolución temporal), con 10 minutos finales de puesta en común de las tendencias observadas por cada pareja.

**Sesión 3 (55 min):**
- Actividad 4 completa (comparativa por provincia).
- 15 min finales: debate guiado sobre determinantes sociales de la salud y por qué existen diferencias territoriales.
- Recogida del entregable.

### Orientaciones metodológicas
- Trabajar en parejas fomenta la discusión sobre interpretación, que es el objetivo de aprendizaje más difícil de alcanzar de forma individual.
- Si el grupo tiene dificultades técnicas con la limpieza de datos, se puede facilitar el dataset ya limpio y centrar el tiempo en la interpretación (Actividades 3 y 4).
- Es un buen momento para introducir, de forma transversal, el debate sobre desinformación en vacunas y el papel del profesional sanitario en la comunicación basada en evidencia.
- Adaptación DUA (Diseño Universal para el Aprendizaje): el alumnado con mayor dificultad técnica puede optar por el nivel Básico (Excel) sin perder los mismos resultados de aprendizaje; el alumnado con mayor autonomía puede ampliar con el notebook Python y explorar otras vacunas del calendario.

### Solución orientativa (para contraste, no para entregar al alumnado)
El dataset de coberturas de vacunación de Castilla y León muestra, de forma general, coberturas superiores al 95% para las vacunas del calendario infantil sistemático en la mayoría de provincias, con descensos puntuales en el bienio 2020-2021 asociados a la pandemia de COVID-19, y cierta variabilidad interanual y territorial entre zonas rurales y urbanas. Los valores exactos dependen del año y la vacuna consultada en el dataset en el momento de la descarga; se recomienda que el profesorado ejecute el notebook con antelación para tener las cifras concretas de la sesión.

### Errores frecuentes del alumnado y cómo abordarlos
- Confundir "número de dosis administradas" con "porcentaje de cobertura": recordar que la cobertura siempre se calcula sobre una población objetivo, no es un recuento absoluto.
- Comparar provincias sin tener en cuenta el tamaño de la población: insistir en que se comparan porcentajes, no números absolutos de vacunados.
- Extraer conclusiones causales sin evidencia suficiente ("esta provincia vacuna menos porque..."): fomentar el uso de "podría deberse a" y pedir que propongan cómo verificarían esa hipótesis.

### Criterios de evaluación
Ver rúbrica de evaluación común en `rubricas/rubricas_evaluacion.md`, apartado Taller 1. Ponderación orientativa: 30% control de calidad de datos, 40% análisis y visualización, 30% interpretación y reflexión.
