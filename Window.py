import sys

from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, \
    QTextEdit, QGroupBox, QFormLayout

import PetrolStation
from PetrolStation import start

app = QApplication(sys.argv)

textBoxTableDiesel = [QLineEdit("10000"), QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"), QLineEdit("50"),
                      QLineEdit("2"), QLineEdit("30"), QLineEdit("5"), QLineEdit("25"), QLineEdit("10"),
                      QLineEdit("30")]

ResultsDiesel = QTextEdit()
Results9598 = QTextEdit()
ResultsGas = QTextEdit()

GroupBoxFormDiesel = QGroupBox("Diesel pump")
GroupBoxForm9598 = QGroupBox("95/98")
GroupBoxFormGas = QGroupBox("Gas")

GroupBoxResultsDiesel = QGroupBox("Results diesel")
GroupBoxResults9598 = QGroupBox("Results 95/98")
GroupBoxResultsGas = QGroupBox("Results gas")

calculateButton = QPushButton("Calculate")


def set_diesel_properties():
    PetrolStation.SIM_TIME = int(textBoxTableDiesel[0].text())
    PetrolStation.GAS_STATION_SIZE = int(textBoxTableDiesel[1].text())
    PetrolStation.THRESHOLD = int(textBoxTableDiesel[2].text())
    PetrolStation.NUMBER_OF_PUMP = int(textBoxTableDiesel[3].text())
    PetrolStation.FUEL_TANK_SIZE = int(textBoxTableDiesel[4].text())
    PetrolStation.REFUELING_SPEED = int(textBoxTableDiesel[5].text())
    PetrolStation.TANK_TRUCK_TIME = int(textBoxTableDiesel[6].text())
    PetrolStation.FUEL_TANK_LEVEL = [int(textBoxTableDiesel[7].text()), int(textBoxTableDiesel[8].text())]
    PetrolStation.T_INTER = [int(textBoxTableDiesel[9].text()), int(textBoxTableDiesel[10].text())]
    start()
    ResultsDiesel.append(PetrolStation.TEXT)


def set_calculate_button():
    calculateButton.clicked.connect(set_diesel_properties)


def set_form_diesel():
    formDiesel = QFormLayout()
    formDiesel.addRow("SIM_TIME", textBoxTableDiesel[0])
    formDiesel.addRow("GAS_STATION_SIZE", textBoxTableDiesel[1])
    formDiesel.addRow("THRESHOLD [%]", textBoxTableDiesel[2])
    formDiesel.addRow("NUMBER_OF_PUMP", textBoxTableDiesel[3])
    formDiesel.addRow("FUEL_TANK_SIZE", textBoxTableDiesel[4])
    formDiesel.addRow("TANK_TRUCK_TIME", textBoxTableDiesel[5])
    formDiesel.addRow("TANK_TRUCK_TIME", textBoxTableDiesel[6])
    formDiesel.addRow("FUEL_TANK_LEVEL_MIN", textBoxTableDiesel[7])
    formDiesel.addRow("FUEL_TANK_LEVEL_MAX", textBoxTableDiesel[8])
    formDiesel.addRow("T_INTER_MIN", textBoxTableDiesel[9])
    formDiesel.addRow("T_INTER_MAX", textBoxTableDiesel[10])
    GroupBoxFormDiesel.setLayout(formDiesel)


def set_grid_result_diesel():
    gridResultDiesel = QGridLayout()
    gridResultDiesel.addWidget(ResultsDiesel, 0, 0)
    GroupBoxResultsDiesel.setLayout(gridResultDiesel)


def set_grid_result_9598():
    gridResult9598 = QGridLayout()
    gridResult9598.addWidget(Results9598, 0, 0)
    GroupBoxResults9598.setLayout(gridResult9598)


def set_grid_result_gas():
    gridResultGas = QGridLayout()
    gridResultGas.addWidget(ResultsGas, 0, 0)
    GroupBoxResultsGas.setLayout(gridResultGas)


def set_layout_window():
    layoutWindow = QGridLayout()
    layoutWindow.addWidget(GroupBoxFormDiesel, 0, 0)
    layoutWindow.addWidget(GroupBoxForm9598, 0, 1)
    layoutWindow.addWidget(GroupBoxFormGas, 0, 2)
    layoutWindow.addWidget(calculateButton, 1, 0, 1, 3)
    layoutWindow.addWidget(GroupBoxResultsDiesel, 2, 0)
    layoutWindow.addWidget(GroupBoxResults9598, 2, 1)
    layoutWindow.addWidget(GroupBoxResultsGas, 2, 2)
    return layoutWindow


class Window:
    window = QWidget()
    set_calculate_button()

    set_form_diesel()

    set_grid_result_diesel()
    set_grid_result_9598()
    set_grid_result_gas()

    window.setLayout(set_layout_window())
    window.show()


app.exec_()
