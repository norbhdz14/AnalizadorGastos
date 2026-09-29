import csv
import os
from datetime import datetime

ARCHIVO_DATOS = "gastos.csv"
CAMPOS = ["fecha", "categoria", "monto", "descripcion"]

def inicializar_archivo():
    """Crea el archivo CSV con encabezados si no existe."""
    if not os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()

def registrar_gasto():
    """Captura los datos de un nuevo gasto y los guarda en el CSV."""
    print("\n--- Registrar Nuevo Gasto ---")
    categoria = input("Categoría (ej. Comida, Transporte, Ocio): ").strip().capitalize()
    
    while True:
        try:
            monto = float(input("Monto ($): "))
            if monto <= 0:
                print("El monto debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    descripcion = input("Descripción breve: ").strip()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(ARCHIVO_DATOS, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writerow({
            "fecha": fecha,
            "categoria": categoria,
            "monto": f"{monto:.2f}",
            "descripcion": descripcion
        })

    print("¡Gasto registrado con éxito!")

def ver_historial():
    """Muestra todas las transacciones guardadas."""
    print("\n--- Historial de Gastos ---")
    if not os.path.exists(ARCHIVO_DATOS):
        print("Aún no hay datos registrados.")
        return

    with open(ARCHIVO_DATOS, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        filas = list(reader)
        if not filas:
            print("No hay gastos registrados.")
            return

        print(f"{'Fecha':<17} | {'Categoría':<12} | {'Monto ($)':<10} | {'Descripción'}")
        print("-" * 60)
        for row in filas:
            print(f"{row['fecha']:<17} | {row['categoria']:<12} | ${float(row['monto']):<9.2f} | {row['descripcion']}")

def resumen_por_categoria():
    """Agrupa y suma los gastos por categoría."""
    print("\n--- Resumen por Categoría ---")
    if not os.path.exists(ARCHIVO_DATOS):
        print("Aún no hay datos registrados.")
        return

    totales = {}
    total_general = 0.0

    with open(ARCHIVO_DATOS, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["categoria"]
            monto = float(row["monto"])
            totales[cat] = totales.get(cat, 0.0) + monto
            total_general += monto

    if not totales:
        print("No hay registros para analizar.")
        return

    for cat, total in totales.items():
        porcentaje = (total / total_general) * 100
        print(f"• {cat:<12}: ${total:>8.2f} ({porcentaje:.1f}%)")

    print("-" * 40)
    print(f"TOTAL GENERAL : ${total_general:.2f}")

def menu():
    """Loop principal de la aplicación."""
    inicializar_archivo()
    while True:
        print("\n==============================")
        print("  ANALIZADOR DE GASTOS (CLI)  ")
        print("==============================")
        print("1. Registrar gasto")
        print("2. Ver historial completo")
        print("3. Ver resumen por categoría")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            resumen_por_categoria()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
