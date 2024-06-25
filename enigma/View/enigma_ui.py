from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit, QMessageBox, QLineEdit, QFileDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class EnigmaUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Máquina Enigma By Jose Freddy Rosas Almendras")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        main_layout = QVBoxLayout()

        # Title
        title = QLabel("Máquina Enigma")
        title.setFont(QFont('Arial', 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Message input
        self.input_message = QLineEdit(self)
        self.input_message.setPlaceholderText("Ingrese el mensaje...")
        self.input_message.setFont(QFont('Arial', 14))
        main_layout.addWidget(self.input_message)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        # Encrypt button
        encrypt_button = QPushButton("Encriptar Mensaje", self)
        encrypt_button.setFont(QFont('Arial', 14))
        encrypt_button.setStyleSheet("background-color: #3498db; color: white; padding: 10px;")
        encrypt_button.clicked.connect(self.encrypt_message)
        buttons_layout.addWidget(encrypt_button)

        # Decrypt button
        decrypt_button = QPushButton("Desencriptar Mensaje", self)
        decrypt_button.setFont(QFont('Arial', 14))
        decrypt_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px;")
        decrypt_button.clicked.connect(self.decrypt_message)
        buttons_layout.addWidget(decrypt_button)

        # Add rotor button
        add_rotor_button = QPushButton("Agregar Rotor", self)
        add_rotor_button.setFont(QFont('Arial', 14))
        add_rotor_button.setStyleSheet("background-color: #f39c12; color: white; padding: 10px;")
        add_rotor_button.clicked.connect(self.add_rotor)
        buttons_layout.addWidget(add_rotor_button)

        # Show rotors button
        show_rotors_button = QPushButton("Mostrar Rotores", self)
        show_rotors_button.setFont(QFont('Arial', 14))
        show_rotors_button.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px;")
        show_rotors_button.clicked.connect(self.show_rotors)
        buttons_layout.addWidget(show_rotors_button)

        # Encrypt file button
        encrypt_file_button = QPushButton("Encriptar Archivo", self)
        encrypt_file_button.setFont(QFont('Arial', 14))
        encrypt_file_button.setStyleSheet("background-color: #2ecc71; color: white; padding: 10px;")
        encrypt_file_button.clicked.connect(self.encrypt_file)
        buttons_layout.addWidget(encrypt_file_button)

        # Decrypt file button
        decrypt_file_button = QPushButton("Desencriptar Archivo", self)
        decrypt_file_button.setFont(QFont('Arial', 14))
        decrypt_file_button.setStyleSheet("background-color: #e67e22; color: white; padding: 10px;")
        decrypt_file_button.clicked.connect(self.decrypt_file)
        buttons_layout.addWidget(decrypt_file_button)

        # Add buttons layout to main layout
        main_layout.addLayout(buttons_layout)

        # Message output
        self.output_message = QTextEdit(self)
        self.output_message.setFont(QFont('Arial', 14))
        self.output_message.setReadOnly(True)
        main_layout.addWidget(self.output_message)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # General style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QPushButton {
                border: none;
                border-radius: 5px;
                margin: 5px;
            }
            QPushButton:hover {
                opacity: 0.8;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #ced4da;
                border-radius: 5px;
                padding: 10px;
            }
        """)

    def encrypt_message(self):
        message = self.input_message.text()
        if message:
            encrypted_message = self.controller.modelo.encriptar_mensaje(message)
            self.output_message.setText(encrypted_message)
        else:
            self.show_error("Por favor, ingrese un mensaje para encriptar.")

    def decrypt_message(self):
        message = self.input_message.text()
        if message:
            decrypted_message = self.controller.modelo.desencriptar_mensaje(message)
            self.output_message.setText(decrypted_message)
        else:
            self.show_error("Por favor, ingrese un mensaje para desencriptar.")

    def add_rotor(self):
        self.controller.modelo.agregar_rotor()
        self.show_info("Rotor agregado exitosamente.")

    def show_rotors(self):
        rotors = '\n\n'.join([f"Rotor {i+1}: {''.join(rotor)}" for i, rotor in enumerate(self.controller.modelo.rotores)])
        self.output_message.setText(rotors)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message, QMessageBox.StandardButton.Ok)

    def show_info(self, message):
        QMessageBox.information(self, "Info", message, QMessageBox.StandardButton.Ok)

    def encrypt_file(self):
        input_path, _ = QFileDialog.getOpenFileName(self, "Seleccione el archivo para encriptar")
        if input_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo encriptado")
            if output_path:
                self.controller.modelo.encriptar_archivo(input_path, output_path)
                self.show_info(f"Archivo encriptado y guardado en {output_path}")

    def decrypt_file(self):
        input_path, _ = QFileDialog.getOpenFileName(self, "Seleccione el archivo para desencriptar")
        if input_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo desencriptado")
            if output_path:
                self.controller.modelo.desencriptar_archivo(input_path, output_path)
                self.show_info(f"Archivo desencriptado y guardado en {output_path}")
