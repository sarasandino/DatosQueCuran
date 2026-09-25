# Datos que Curan
### Taller de análisis de datos sanitarios para FP de Salud

**Autora:** Sara Sandino González
**Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Concurso Datos Abiertos de la Comunidad de Castilla y León 2026** · Categorías Ideas y Recurso Didáctico

---

## Presentación

Datos que Curan es un recurso didáctico abierto para el alumnado de Formación Profesional de Salud que introduce el análisis de datos a través de **datos abiertos sanitarios reales de Castilla y León**: vacunación, listas de espera quirúrgica, atención primaria y farmacia.

No requiere conocimientos previos de programación ni de estadística avanzada. Cada taller se ofrece en dos niveles —**Básico (Excel/Calc)** y **Avanzado (Python/Jupyter)**— para adaptarse a la diversidad de perfiles y ciclos formativos de la familia profesional de Sanidad.

## A quién va dirigido

| Ciclo formativo | Módulos de conexión sugeridos |
|---|---|
| CFGM Cuidados Auxiliares de Enfermería | Técnicas de Ayuda Odontológica/Estomatológica, FOL |
| CFGM Farmacia y Parafarmacia | Dispensación de Productos Farmacéuticos, Oficina de Farmacia |
| CFGS Documentación y Administración Sanitarias | Gestión de Pacientes, Documentación Sanitaria, Sistemas de Información Sanitaria |
| CFGS Laboratorio Clínico y Biomédico | Gestión de Muestras Biológicas, Control de Calidad |
| CFGS Salud Ambiental / Higiene Bucodental | Epidemiología, Educación para la Salud |

También es adaptable a asignaturas de Bachillerato de Ciencias con orientación sanitaria y a primeros cursos de Grados universitarios de Salud Pública o Gestión Sanitaria.

## Estructura del repositorio

```
datos-que-curan/
├── README.md
├── LICENSE.md
├── requisitos.txt
├── taller1_vacunacion/
│   ├── guia_alumnado.md
│   ├── guia_profesorado.md
│   ├── notebook_taller1.py      (celdas listas para Jupyter)
│   └── datos/                   (el alumnado descarga aquí el CSV)
├── taller2_listas_espera/
│   ├── guia_alumnado.md
│   ├── guia_profesorado.md
│   ├── notebook_taller2.py
│   └── datos/
├── taller3_farmacia/
│   ├── guia_alumnado.md
│   ├── guia_profesorado.md
│   ├── notebook_taller3.py
│   └── datos/
├── taller4_proyecto_final/
│   ├── guia_alumnado.md
│   └── guia_profesorado.md
└── rubricas/
    └── rubricas_evaluacion.md
```

## Los 4 talleres

| Taller | Título | Dataset JCyL | Duración | Resultado de aprendizaje principal |
|---|---|---|---|---|
| 1 | Coberturas de vacunación | `coberturas-de-vacunacion-en-castilla-y-leon` | 3 sesiones | Analizar series temporales e interpretar indicadores de salud pública |
| 2 | Listas de espera quirúrgica | Catálogo Lista de espera quirúrgica (Sanidad CyL) | 3 sesiones | Comparar variables categóricas y detectar desigualdades territoriales |
| 3 | Farmacia y dispensaciones | `consumo-de-productos-farmaceuticos-por-receta` | 2 sesiones | Identificar estacionalidad y patrones de consumo |
| 4 | Proyecto final autónomo | A elección del alumnado, catálogo completo de Salud | 4 sesiones | Diseñar y comunicar un análisis de datos sanitario propio |

Todos los datasets provienen del [Portal de Datos Abiertos de la Junta de Castilla y León](https://datosabiertos.jcyl.es) y son explotables desde el [portal de análisis de datos](https://analisis.datosabiertos.jcyl.es).

## Requisitos técnicos

- **Nivel Básico**: Excel, LibreOffice Calc o Google Sheets. No requiere instalación adicional.
- **Nivel Avanzado**: Python 3.9+, con las librerías indicadas en `requisitos.txt` (`pandas`, `matplotlib`, `numpy`, `jupyter`). Se recomienda usar [Google Colab](https://colab.research.google.com) si el centro no dispone de Python instalado en los equipos, ya que no requiere instalación y es gratuito.

## Metodología

El recurso sigue un enfoque de **aprendizaje basado en datos reales** (data-driven learning) con progresión pedagógica en tres fases por taller: comprensión del dato clínico/sanitario, tratamiento técnico del dato (limpieza, cálculo, visualización) y transferencia profesional (interpretación aplicada al contexto laboral del ciclo). Cada notebook incluye celdas de comprobación ("checkpoints") para que el alumnado valide su progreso antes de avanzar.

## Licencia

Este recurso se publica bajo licencia **CC BY 4.0**. Puede copiarse, redistribuirse, adaptarse y usarse con cualquier fin, incluso comercial, mencionando la autoría original y enlazando a este repositorio. Los datos de origen conservan sus licencias propias del Portal de Datos Abiertos de la Junta de Castilla y León.

## Autoría

Proyecto presentado al Concurso de Datos Abiertos de la Comunidad de Castilla y León 2026, categorías Ideas y Recurso Didáctico, por Sara Sandino González (saragsandino@gmail.com).
