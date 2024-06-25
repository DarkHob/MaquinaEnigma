class EnigmaView:
    def mostrar_menu(self):
        print("\nSeleccione una opción:")
        print("1. Encriptar un mensaje")
        print("2. Desencriptar un mensaje")
        print("3. Agregar un rotor")
        print("4. Mostrar rotores")
        print("5. Salir")

    def obtener_opcion(self):
        return input("Ingrese el número de la opción: ")

    def obtener_mensaje(self, tipo):
        return input(f"Ingrese el mensaje a {tipo}: ")

    def mostrar_mensaje(self, tipo, mensaje):
        print(f"Mensaje {tipo}:", mensaje)

    def mostrar_rotores(self, rotores):
        for i, rotor in enumerate(rotores, start=1):
            print(f"Rotor {i}:", rotor)
