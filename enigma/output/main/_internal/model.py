import random

class EnigmaModel:
    def __init__(self):
        self.rotores = [self._generar_rotor() for _ in range(3)]

    def _generar_rotor(self):
        caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+ñ"
        rotor = list(caracteres)
        random.shuffle(rotor)
        return rotor

    def encriptar_mensaje(self, mensaje):
        return self._procesar_mensaje(mensaje, encriptar=True)

    def desencriptar_mensaje(self, mensaje):
        return self._procesar_mensaje(mensaje, encriptar=False)

    def _procesar_mensaje(self, mensaje, encriptar):
        resultado = []
        for i, char in enumerate(mensaje):
            rotor = self.rotores[i % len(self.rotores)]
            if encriptar:
                if char in rotor:
                    index = rotor.index(char)
                    resultado.append(rotor[(index + 1) % len(rotor)])
                else:
                    resultado.append(char)
            else:
                if char in rotor:
                    index = rotor.index(char)
                    resultado.append(rotor[(index - 1) % len(rotor)])
                else:
                    resultado.append(char)
        return ''.join(resultado)

    def agregar_rotor(self):
        self.rotores.append(self._generar_rotor())

    def mostrar_rotores(self):
        for i, rotor in enumerate(self.rotores):
            print(f"Rotor {i+1}: {''.join(rotor)}")

    def encriptar_archivo(self, input_path, output_path):
        with open(input_path, 'r', encoding='utf-8') as file:
            contenido = file.read()
        contenido_encriptado = self.encriptar_mensaje(contenido)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(contenido_encriptado)

    def desencriptar_archivo(self, input_path, output_path):
        with open(input_path, 'r', encoding='utf-8') as file:
            contenido = file.read()
        contenido_desencriptado = self.desencriptar_mensaje(contenido)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(contenido_desencriptado)
