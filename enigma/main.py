import sys
import os

# Agregar rutas para importar controller, model y view
sys.path.append(os.path.join(os.path.dirname(__file__), 'Controller'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Model'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'View'))

from controller import EnigmaController
from model import EnigmaModel
from view import EnigmaView

if __name__ == "__main__":
    modelo = EnigmaModel()
    vista = EnigmaView()
    controlador = EnigmaController(modelo, vista)

    # Opción para ejecutar GUI o CLI
    modo = input("Seleccione el modo (1: CLI, 2: GUI): ")
    if modo == "1":
        controlador.ejecutar()
    elif modo == "2":
        controlador.ejecutar_gui()
    else:
        print("Opción no válida. Saliendo...")
