import sys
from pathlib import Path
import csv

#!/usr/bin/env python3
"""
MiTiendita POS - Command Line Interface
A simple point of sale system for small businesses.
"""

def read_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = csv.reader(file, delimiter=',')
            prices = list(data)
            for i in range(1, len(prices)):
                for j in range(len(prices[i])):
                    print(prices[0][j] + ": " + prices[i][j])
                print('')
    except FileNotFoundError:
        print(f"No se encontro el archivo: {file_path}")

def write_csv(file_path, data):
    try:
        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def main():
    print("Bienvenido a MiTiendita POS")
    print("=" * 40)

    # Menu principal
    
    while True:
        print("\nMenú principal:")
        print("1. Nueva compra")
        print("2. Ver productos")
        print("3. Inventario")
        print("4. Reportes")
        print("5. Configuración")
        print("6. Salir")
        
        choice = input("\nSeleccione una opción: ").strip()
        
        match choice:
            case "1":
                print("Cargando el catálogo...")
                # Leer archivo productos.csv
                catalogo_csv = "productos.csv"
                read_csv(catalogo_csv)

                # Seleccionar productos para la compra


            case "2":
                print("Cargando el catálogo...")
                # Leer archivo productos.csv
                catalogo_csv = "productos.csv"
                read_csv(catalogo_csv)
               
            # TODO: Implementar la funcionalidad de inventario
            case "3":
                while True:
                    print("\nMenú de Inventario:")
                    print("1. Ver inventario")
                    print("2. Agregar producto")
                    print("3. Eliminar producto")
                    print("4. Volver al menú principal")
                    
                    inv_choice = input("\nSeleccione una opción: ").strip()
                    
                    match inv_choice:
                        case "1":
                            print("Cargando el catálogo...")
                            # Leer archivo productos.csv
                            catalogo_csv = "productos.csv"
                            read_csv(catalogo_csv)
                        case "2":
                            print("Ingrese el nombre del nuevo producto:")
                            nuevo_producto = input().strip()
                            print("Ingrese el precio del nuevo producto:")
                            precio_producto = input().strip()
                            print(f"El producto '{nuevo_producto}' con precio '{precio_producto}' sera agregado al inventario.")
                            print("Desea agregar otro producto? (s/n)")

                        case "3":
                            print("Funcionalidad de eliminar producto no implementada aún.")
                        case "4":
                            break
                        case _:
                            print("Opción inválida. Por favor, inténtelo de nuevo.")


                """
                print("Funcionalidad de inventario no implementada aún.")
                print("¿Desea realizar otra operación? (s/n)")
                again = input().strip().lower()
                if again != "s":
                    print("Gracias por usar MiTiendita POS")
                    sys.exit(0)
                else:
                    continue
                """
    
            case "4":
                print("Funcionalidad de reportes no implementada aún.")
            case "5":
                print("Funcionalidad de configuración no implementada aún.")
            case "6":
                print("Gracias por usar MiTiendita POS")
                sys.exit(0)
            case _:
                print("Opción inválida. Por favor, inténtelo de nuevo.")


if __name__ == "__main__":
    main()