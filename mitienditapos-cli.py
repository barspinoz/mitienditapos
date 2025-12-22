import sys
from pathlib import Path

#!/usr/bin/env python3
"""
MiTiendita POS - Command Line Interface
A simple point of sale system for small businesses.
"""



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
                products_file = Path("productos.csv")
                if not products_file.exists():
                    print("Error: no se encontró el archivo productos.csv.")
                    continue
                with products_file.open("r", encoding="utf-8") as f:
                    products = f.readlines()
                print(f"Se cargaron {len(products)} productos.")
                # Seleccionar productos y calcular total
                total = 0.0
                for product in products:
                    try:
                        parts = product.strip().split(",")
                        if len(parts) < 2:
                            continue
                        name, price = parts[0], parts[1]
                        price = float(price)
                        print(f"Producto: {name}, Precio: ${price:.2f}")
                        total += price
                    except (ValueError, IndexError):
                        continue
                print(f"Total de la compra: ${total:.2f}")
                print("¿Desea realizar otra operación? (s/n)")
                again = input().strip().lower()
                if again != "s":
                    print("Gracias por usar MiTiendita POS")
                    sys.exit(0)
                else:
                    continue

            case "2":
                print("Cargando el catálogo...")
                # Leer archivo productos.csv
                products_file = Path("productos.csv")
                if not products_file.exists():
                    print("Error: no se encontró el archivo productos.csv.")
                    continue
                with products_file.open("r", encoding="utf-8") as f:
                    products = f.readlines()
                # Mostrar productos
                for product in products:
                    try:
                        parts = product.strip().split(",")
                        if len(parts) < 2:
                            continue
                        name, price = parts[0], parts[1]
                        price = float(price)
                        print(f"Producto: {name}, Precio: ${price:.2f}")
                    except (ValueError, IndexError):
                        continue
                print(f"Se cargaron {len(products)} productos.")
                # Mostrar productos
                for product in products:
                    name, price = product.strip().split(",")
                    price = float(price)
                    print(f"Producto: {name}, Precio: ${price:.2f}")
                print("¿Desea realizar otra operación? (s/n)")
                again = input().strip().lower()
                if again != "s":
                    print("Gracias por usar MiTiendita POS")
                    sys.exit(0)
                else:
                    continue
        
            case "3":
                print("Funcionalidad de inventario no implementada aún.")
                print("¿Desea realizar otra operación? (s/n)")
                again = input().strip().lower()
                if again != "s":
                    print("Gracias por usar MiTiendita POS")
                    sys.exit(0)
                else:
                    continue
    
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