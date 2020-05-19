import sys
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QGroupBox

import PetrolStation
from PetrolStation import start

app = QApplication(sys.argv)
label1 = QLabel("SIM_TIME")
label2 = QLabel("GAS_STATION_SIZE")
label3 = QLabel("THRESHOLD [%]")
label4 = QLabel("NUMBER_OF_PUMP")
label5 = QLabel("FUEL_TANK_SIZE")
label6 = QLabel("REFUELING_SPEED")
label7 = QLabel("TANK_TRUCK_TIME")
label8 = QLabel("FUEL_TANK_LEVEL_MIN")
label9 = QLabel("FUEL_TANK_LEVEL_MAX")
label10 = QLabel("T_INTER_MIN")
label11 = QLabel("T_INTER_MAX")

textBox1 = QLineEdit("10000")
textBox2 = QLineEdit("2000")
textBox3 = QLineEdit("10")
textBox4 = QLineEdit("2")
textBox5 = QLineEdit("50")
textBox6 = QLineEdit("2")
textBox7 = QLineEdit("30")
textBox8 = QLineEdit("5")
textBox9 = QLineEdit("25")
textBox10 = QLineEdit("10")
textBox11 = QLineEdit("30")

bigEditor = QTextEdit()


def say_hello():
    PetrolStation.SIM_TIME = int(textBox1.text())
    PetrolStation.GAS_STATION_SIZE = int(textBox2.text())
    PetrolStation.THRESHOLD = int(textBox3.text())
    PetrolStation.NUMBER_OF_PUMP = int(textBox4.text())
    PetrolStation.FUEL_TANK_SIZE = int(textBox5.text())
    PetrolStation.REFUELING_SPEED = int(textBox6.text())
    PetrolStation.TANK_TRUCK_TIME = int(textBox7.text())
    PetrolStation.FUEL_TANK_LEVEL = [int(textBox8.text()), int(textBox9.text())]
    PetrolStation.T_INTER = [int(textBox10.text()), int(textBox11.text())]

    start()
    bigEditor.append(PetrolStation.TEXT)


class Window:

    window = QWidget()

    button1 = QPushButton("Calculate")

    button1.clicked.connect(say_hello)

    layout = QGridLayout()
    layout.addWidget(label1, 0, 0)
    layout.addWidget(textBox1, 0, 1)
    layout.addWidget(label2, 1, 0)
    layout.addWidget(textBox2, 1, 1)
    layout.addWidget(label3, 2, 0)
    layout.addWidget(textBox3, 2, 1)
    layout.addWidget(label4, 3, 0)
    layout.addWidget(textBox4, 3, 1)
    layout.addWidget(label5, 4, 0)
    layout.addWidget(textBox5, 4, 1)
    layout.addWidget(label6, 5, 0)
    layout.addWidget(textBox6, 5, 1)
    layout.addWidget(label7, 6, 0)
    layout.addWidget(textBox7, 6, 1)
    layout.addWidget(label8, 7, 0)
    layout.addWidget(textBox8, 7, 1)
    layout.addWidget(label9, 8, 0)
    layout.addWidget(textBox9, 8, 1)
    layout.addWidget(label10, 9, 0)
    layout.addWidget(textBox10, 9, 1)
    layout.addWidget(label11, 10, 0)
    layout.addWidget(textBox11, 10, 1)

    layout.addWidget(button1, 11, 0, 1, 2)
    layout.addWidget(bigEditor, 12, 0, 1, 2)

    window.setLayout(layout)
    window.show()


app.exec_()
