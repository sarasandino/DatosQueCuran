# Guía de la versión Excel/Calc

Este documento explica cómo replicar en Excel o LibreOffice Calc el mismo análisis que se hace en los notebooks de Python de los Talleres 1, 2 y 3, sin necesidad de programar. Está pensado para grupos que trabajan la versión básica del recurso.

## Cómo empezar (válido para los tres talleres)

1. Descarga el CSV del dataset correspondiente desde el Portal de Datos Abiertos de la Junta de Castilla y León (ver enlace de cada taller en su guía de alumnado).
2. Abre Excel o LibreOffice Calc y usa **Datos → Desde texto/CSV** (Excel) o **Archivo → Abrir** (Calc) para importar el archivo. Comprueba el separador de columnas (los CSV de JCyL suelen usar punto y coma `;`).
3. Convierte el rango de datos en una **tabla** (Excel: Insertar → Tabla; Calc: Datos → Definir intervalo de base de datos). Esto facilita aplicar filtros y que las fórmulas se ajusten automáticamente si añades filas.
4. A partir de aquí, sigue las instrucciones específicas de cada taller.

## Taller 1 · Coberturas de vacunación

**Actividad 2 (control de calidad):** usa **Datos → Filtro** para revisar visualmente si hay celdas vacías en la columna de cobertura, y **Formato condicional → Resaltar reglas de celdas → Menor que / Mayor que** para marcar en rojo cualquier valor de cobertura fuera del rango 0-100%.

**Actividad 3 (evolución temporal):** la forma más rápida es crear una **tabla dinámica** (Insertar → Tabla dinámica): arrastra `año` a Filas, `cobertura` a Valores (configurada como Promedio) y `vacuna` a Filtros para poder elegir una vacuna concreta. Con la tabla dinámica seleccionada, inserta un **gráfico de líneas** (Insertar → Gráfico dinámico o gráfico normal a partir de la tabla).

Alternativa con fórmula, si prefieres no usar tabla dinámica: `=PROMEDIO.SI.CONJUNTO(rango_cobertura; rango_vacuna; "Hexavalente"; rango_año; año_celda)`.

**Actividad 4 (comparativa por provincia):** repite el mismo proceso de tabla dinámica, pero con `provincia` en Filas en lugar de `año`, filtrando por el último año disponible y la vacuna elegida. Añade una **columna calculada** con la fórmula `=SI(cobertura<95;"Por debajo";"OK")` para destacar visualmente las provincias en riesgo, y usa **Formato condicional** para colorear esas filas.

## Taller 2 · Listas de espera quirúrgica

**Actividad 2 (tiempo medio por especialidad):** tabla dinámica con `especialidad` en Filas y `tiempo_medio_espera_dias` en Valores (Promedio). Ordena la tabla de mayor a menor (clic derecho sobre la columna de valores → Ordenar) e inserta un gráfico de **barras horizontales** directamente desde la tabla dinámica.

Fórmula equivalente: `=PROMEDIO.SI(rango_especialidad; "Traumatología"; rango_tiempo_espera)`.

**Actividad 3 (comparativa por provincia):** tabla dinámica con `provincia` en Filas, `especialidad` en Columnas (filtrando solo las 3 especialidades con más espera de la Actividad 2) y `tiempo_medio_espera_dias` en Valores. El gráfico de **barras agrupadas** que genera Excel/Calc directamente desde esta tabla dinámica es exactamente el que se busca en esta actividad.

**Actividad 4 (comparación con media nacional):** simplemente añade una celda con el valor de referencia nacional (buscado manualmente en el informe SISNS) y calcula la diferencia con `=PROMEDIO(rango_tiempo_espera) - celda_referencia_nacional`.

## Taller 3 · Farmacia y medicamentos

**Actividad 3 (consumo por tipo de producto):** tabla dinámica con `tipo_producto` en Filas y `numero_envases` en Valores (Suma). Gráfico de barras verticales desde la tabla dinámica.

Fórmula equivalente: `=SUMA.SI(rango_tipo_producto; "Medicamentos respiratorios"; rango_envases)`.

**Actividad 4 (patrón estacional):** este es el paso que requiere más cuidado en Excel, porque hay que agrupar por mes ignorando el año. La forma más sencilla:
1. Añade una columna auxiliar con la fórmula `=MES(fecha_celda)` para extraer solo el número de mes (1-12) de cada fila.
2. Crea una tabla dinámica con esa columna auxiliar de mes en Filas, `numero_envases` en Valores (Suma), y un filtro por `tipo_producto` = "Medicamentos respiratorios".
3. Inserta un gráfico de **líneas** con los 12 meses en el eje X. Si ves que enero y diciembre tienen valores altos y los meses de verano bajos, ese es el patrón estacional que se busca en esta actividad.

## Consejos generales para el profesorado

- Si el grupo tiene dificultades con tablas dinámicas, se puede sustituir por las fórmulas equivalentes (`PROMEDIO.SI.CONJUNTO`, `SUMA.SI.CONJUNTO`, `PROMEDIO.SI`, `SUMA.SI`) copiándolas celda a celda; es más manual pero refuerza mejor la lógica del cálculo.
- LibreOffice Calc usa los mismos nombres de función que Excel en español (`PROMEDIO.SI.CONJUNTO`, `SUMA.SI.CONJUNTO`), por lo que esta guía es válida para ambos programas sin cambios.
- Para todos los gráficos, recuerda añadir siempre título, etiquetas de los ejes y, cuando aplique, una línea de referencia (por ejemplo, el umbral del 95% en el Taller 1) usando una serie de datos adicional con el mismo valor repetido.
