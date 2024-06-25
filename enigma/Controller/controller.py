import sys
import os

# Agregar rutas para importar model y view
sys.path.append(os.path.join(os.path.dirname(__file__), '../Model'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../View'))

from model import EnigmaModel
from view import EnigmaView
from enigma_ui import EnigmaUI
from PyQt6.QtWidgets import QApplication  # Importación de QApplication

class EnigmaController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.obtener_opcion()

            if opcion == "1":
                mensaje = self.vista.obtener_mensaje("encriptar")
                mensaje_encriptado = self.modelo.encriptar_mensaje(mensaje)
                self.vista.mostrar_mensaje("encriptado", mensaje_encriptado)
            elif opcion == "2":
                mensaje_encriptado = self.vista.obtener_mensaje("desencriptar")
                mensaje_desencriptado = self.modelo.desencriptar_mensaje(mensaje_encriptado)
                self.vista.mostrar_mensaje("desencriptado", mensaje_desencriptado)
            elif opcion == "3":
                self.modelo.agregar_rotor()
            elif opcion == "4":
                self.modelo.mostrar_rotores()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def ejecutar_gui(self):
        app = QApplication(sys.argv)
        gui = EnigmaUI(self)
        gui.show()
        sys.exit(app.exec())
