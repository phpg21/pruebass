
"""
Calculadora de Impuestos de Venta
Archivo principal para ejecutar la aplicación
"""

import sys
import os

# Ajustar path para importar desde src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

def ejecutar_consola():
    from src.view.interfaz_consola import main_consola
    main_consola()

def ejecutar_gui():
    from src.view.interfaz_kivy import ImpuestosApp
    ImpuestosApp().run()

if __name__ == "__main__":
    while True:
        print("\nSeleccione el modo de ejecución:")
        print("1. Consola")
        print("2. Interfaz gráfica (Kivy)")

        opcion = input("Ingrese el número de su elección: ").strip()

        if opcion == "1":
            ejecutar_consola()
            break
        elif opcion == "2":
            ejecutar_gui()
            break
        else:
            print(f"Ingresaste el número '{opcion}' y no está entre las opciones. Vuelve a ingresar.")
