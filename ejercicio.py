import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QComboBox

class ControlGastos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Gastos Personales")
        self.setGeometry(200, 200, 400, 300)

        # Lista para almacenar los gastos
        self.gastos = []

        # --- Widgets ---
        self.label_monto = QLabel("Ingrese el monto del gasto:")
        self.input_monto = QLineEdit()

        self.label_categoria = QLabel("Seleccione la categoría:")
        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems(["Comida", "Transporte", "Otros"])

        self.boton_agregar = QPushButton("Agregar gasto")
        self.boton_total = QPushButton("Calcular total")

        self.texto_resultado = QTextEdit()
        self.texto_resultado.setReadOnly(True)  # Solo lectura

        # --- Layout (organización en pantalla) ---
        layout = QVBoxLayout()
        layout.addWidget(self.label_monto)
        layout.addWidget(self.input_monto)
        layout.addWidget(self.label_categoria)
        layout.addWidget(self.combo_categoria)
        layout.addWidget(self.boton_agregar)
        layout.addWidget(self.boton_total)
        layout.addWidget(self.texto_resultado)

        self.setLayout(layout)

        # --- Conexiones de botones ---
        self.boton_agregar.clicked.connect(self.agregar_gasto)
        self.boton_total.clicked.connect(self.calcular_total)

    def agregar_gasto(self):
        """Agrega un gasto a la lista con monto y categoría"""
        try:
            monto = float(self.input_monto.text())  # Convierte el texto a número
            categoria = self.combo_categoria.currentText()
            self.gastos.append((monto, categoria))

            # Mostrar gasto agregado
            self.texto_resultado.append(f"Gasto: ${monto:.2f} - Categoría: {categoria}")

            # Limpiar campo de entrada
            self.input_monto.clear()
        except ValueError:
            self.texto_resultado.append("⚠️ Error: Ingrese un número válido")

    def calcular_total(self):
        """Calcula y muestra el total de los gastos"""
        total = sum(monto for monto, _ in self.gastos)
        self.texto_resultado.append(f"\n💰 Total de gastos: ${total:.2f}\n")

# --- Programa principal ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ControlGastos()
    ventana.show()
    sys.exit(app.exec_())