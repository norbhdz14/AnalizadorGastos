# Analizador de Gastos Personales (CLI)

Un script interactivo en consola desarrollado en Python para gestionar y clasificar tus finanzas diarias sin dependencias externas.

## Características

- **Registro dinámico:** Guarda fecha, categoría, monto y descripción del gasto.
- **Persistencia de datos:** Mantiene el registro en un archivo `gastos.csv`.
- **Análisis por categoría:** Calcula el desglose acumulado y el porcentaje del total gastado por cada categoría.
- **Sin dependencias externas:** Funciona únicamente con la biblioteca estándar de Python.

## Estructura del Proyecto

```text
├── gastos.py      # Script principal con la lógica del programa
├── gastos.csv     # Archivo de base de datos local (auto-generado)
└── README.md      # Documentación del proyecto
