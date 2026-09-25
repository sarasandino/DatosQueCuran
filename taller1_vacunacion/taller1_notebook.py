"""
================================================================================
Taller 1 - Analisis de coberturas de vacunacion en Castilla y Leon
Datos que Curan - Recurso didactico para FP de Salud
Licencia: CC BY 4.0 - Sara Sandino Gonzalez
================================================================================

INSTRUCCIONES PARA EL ALUMNADO:
1. Descarga el CSV del dataset "coberturas-de-vacunacion-en-castilla-y-leon"
   desde analisis.datosabiertos.jcyl.es
2. Guardalo como 'coberturas_vacunacion.csv' en la carpeta 'datos/' de este taller.
3. Ejecuta las celdas en orden, de arriba a abajo. Cada bloque separado por
   '# %%' es una celda independiente si abres este archivo en Jupyter o VS Code.
4. Los bloques marcados como "CHECKPOINT" sirven para comprobar que vas bien
   antes de continuar. Si el resultado no tiene sentido, revisa la celda anterior.
5. Los bloques marcados como "EJERCICIO" los debes completar tu.
================================================================================
"""

# %% Celda 1 - Importar librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# %% Celda 2 - Cargar el dataset
try:
    df = pd.read_csv('datos/coberturas_vacunacion.csv', sep=';', encoding='utf-8')
except FileNotFoundError:
    raise FileNotFoundError(
        "No se encuentra el archivo 'datos/coberturas_vacunacion.csv'. "
        "Descargalo primero desde analisis.datosabiertos.jcyl.es "
        "y guardalo en la carpeta 'datos/' de este taller."
    )

print(f"Dataset cargado correctamente: {df.shape[0]} filas, {df.shape[1]} columnas")
df.head()

# %% Celda 3 - Exploracion inicial (Actividad 1)
print("Columnas disponibles:", df.columns.tolist())
print("\nProvincias en el dataset:", sorted(df['provincia'].unique()))
print("\nVacunas en el dataset:", sorted(df['vacuna'].unique()))
print("\nRango de anios:", df['anio'].min(), "-", df['anio'].max())

# %% CHECKPOINT 1
# Si el paso anterior funciona, deberias ver 9 provincias de Castilla y Leon
# (Avila, Burgos, Leon, Palencia, Salamanca, Segovia, Soria, Valladolid, Zamora)
n_provincias = df['provincia'].nunique()
assert n_provincias <= 9, "Revisa: hay mas de 9 valores distintos de provincia, puede haber errores de escritura"
print(f"Checkpoint OK: {n_provincias} provincias detectadas")

# %% Celda 4 - Control de calidad de datos (Actividad 2)
print("Valores nulos por columna:")
print(df.isnull().sum())

print("\nEstadisticas de la columna 'cobertura':")
print(df['cobertura'].describe())

fuera_de_rango = df[(df['cobertura'] < 0) | (df['cobertura'] > 100)]
print(f"\nFilas con cobertura fuera de rango (0-100%): {len(fuera_de_rango)}")

# %% Celda 5 - Limpieza: normalizar nombres de provincia
df['provincia'] = df['provincia'].str.strip().str.title()
df = df.dropna(subset=['cobertura'])
print(f"Filas tras la limpieza: {len(df)}")

# %% CHECKPOINT 2
assert df['cobertura'].between(0, 100).all(), "Aun hay valores de cobertura fuera de rango"
print("Checkpoint OK: todos los valores de cobertura estan entre 0 y 100")

# %% Celda 6 - Evolucion temporal de una vacuna (Actividad 3)
vacuna_elegida = 'Hexavalente'  # cambia este valor por otra vacuna del dataset si quieres

if vacuna_elegida not in df['vacuna'].unique():
    print(f"Aviso: '{vacuna_elegida}' no esta en el dataset. Vacunas disponibles: {df['vacuna'].unique()}")

evolucion = (
    df[df['vacuna'] == vacuna_elegida]
    .groupby('anio')['cobertura']
    .mean()
    .reset_index()
)

plt.figure(figsize=(8, 5))
plt.plot(evolucion['anio'], evolucion['cobertura'], marker='o', linewidth=2)
plt.axhline(y=95, color='red', linestyle='--', alpha=0.6, label='Umbral inmunidad de grupo (95%)')
plt.title(f'Evolucion de la cobertura de {vacuna_elegida} en Castilla y Leon')
plt.xlabel('Anio')
plt.ylabel('Cobertura (%)')
plt.ylim(0, 105)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('evolucion_cobertura.png', dpi=150)
plt.show()

# %% Celda 7 - Comparativa por provincia en el ultimo anio disponible (Actividad 4)
ultimo_anio = df['anio'].max()
comparativa = (
    df[(df['vacuna'] == vacuna_elegida) & (df['anio'] == ultimo_anio)]
    .groupby('provincia')['cobertura']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))
colores = ['seagreen' if v >= 95 else 'indianred' for v in comparativa.values]
comparativa.plot(kind='bar', color=colores)
plt.axhline(y=95, color='black', linestyle='--', alpha=0.6, label='Umbral inmunidad de grupo (95%)')
plt.title(f'Cobertura de {vacuna_elegida} por provincia ({ultimo_anio})')
plt.ylabel('Cobertura (%)')
plt.legend()
plt.tight_layout()
plt.savefig('comparativa_provincias.png', dpi=150)
plt.show()

# %% Celda 8 - Resumen automatico de resultados
print("="*60)
print("RESUMEN DE RESULTADOS")
print("="*60)
print(f"Vacuna analizada: {vacuna_elegida}")
print(f"Ultimo anio disponible: {ultimo_anio}")
print(f"Provincia con mayor cobertura: {comparativa.idxmax()} ({comparativa.max():.1f}%)")
print(f"Provincia con menor cobertura: {comparativa.idxmin()} ({comparativa.min():.1f}%)")
print(f"Numero de provincias por debajo del 95%: {(comparativa < 95).sum()} de {len(comparativa)}")

# %% EJERCICIO - Completa tu mismo
# Repite el analisis de la Celda 6 y 7 con otra vacuna del dataset (por ejemplo 'DTPa' o 'VPI').
# Compara los resultados con los de la vacuna Hexavalente: ¿la tendencia es parecida?
#
# vacuna_2 = '...'
# (completa aqui tu codigo)
