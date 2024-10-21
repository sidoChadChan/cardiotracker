import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
, QTableWidget, QTableWidgetItem)

class HealthApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ciśnieniomierz")

        layout = QVBoxLayout()

        hbox1 = QHBoxLayout()
        self.systolic_input = QLineEdit(self)
        self.systolic_input.setPlaceholderText("Cisnienie skurczowe")
        self.diastolic_input = QLineEdit(self)
        self.diastolic_input.setPlaceholderText("Ciśnienie rozkurczowe")
        self.pulse_input = QLineEdit(self)
        self.pulse_input.setPlaceholderText("Tętno")

        hbox1.addWidget(self.systolic_input)
        hbox1.addWidget(self.diastolic_input)
        hbox1.addWidget(self.pulse_input)

        layout.addLayout(hbox1)

        self.add_button = QPushButton("Dodaj wynik", self)
        self.add_button.clicked.connect(self.add_result)
        layout.addWidget(self.add_button)

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Skurczowe", "Rozkurczowe", "Tętno"])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_result(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealthApp()
    window.show()
    sys.exit(app.exec_())