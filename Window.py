import sys

from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, \
    QTextEdit, QGroupBox, QFormLayout

import Diesel
from Diesel import startDiesel

import p9598
from p9598 import start9598

import Gas
from Gas import startGas

import NumberOfCarChart

app = QApplication(sys.argv)

textBoxTableDiesel = [QLineEdit("10000"), QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"), QLineEdit("50"),
                      QLineEdit("2"), QLineEdit("30"), QLineEdit("5"), QLineEdit("25"), QLineEdit("10"),
                      QLineEdit("30")]

textBoxTable9598 = [QLineEdit("20000"), QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"), QLineEdit("50"),
                    QLineEdit("2"), QLineEdit("30"), QLineEdit("5"), QLineEdit("25"), QLineEdit("10"),
                    QLineEdit("30")]

textBoxTableGas = [QLineEdit("20000"), QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"), QLineEdit("50"),
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
    Diesel.SIM_TIME = int(textBoxTableDiesel[0].text())
    Diesel.GAS_STATION_SIZE = int(textBoxTableDiesel[1].text())
    Diesel.THRESHOLD = int(textBoxTableDiesel[2].text())
    Diesel.NUMBER_OF_PUMP = int(textBoxTableDiesel[3].text())
    Diesel.FUEL_TANK_SIZE = int(textBoxTableDiesel[4].text())
    Diesel.REFUELING_SPEED = int(textBoxTableDiesel[5].text())
    Diesel.TANK_TRUCK_TIME = int(textBoxTableDiesel[6].text())
    Diesel.FUEL_TANK_LEVEL = [int(textBoxTableDiesel[7].text()), int(textBoxTableDiesel[8].text())]
    Diesel.T_INTER = [int(textBoxTableDiesel[9].text()), int(textBoxTableDiesel[10].text())]
    startDiesel()
    ResultsDiesel.append(Diesel.TEXT)


def set_9598_properties():
    p9598.SIM_TIME = int(textBoxTable9598[0].text())
    p9598.GAS_STATION_SIZE = int(textBoxTable9598[1].text())
    p9598.THRESHOLD = int(textBoxTable9598[2].text())
    p9598.NUMBER_OF_PUMP = int(textBoxTable9598[3].text())
    p9598.FUEL_TANK_SIZE = int(textBoxTable9598[4].text())
    p9598.REFUELING_SPEED = int(textBoxTable9598[5].text())
    p9598.TANK_TRUCK_TIME = int(textBoxTable9598[6].text())
    p9598.FUEL_TANK_LEVEL = [int(textBoxTable9598[7].text()), int(textBoxTable9598[8].text())]
    p9598.T_INTER = [int(textBoxTable9598[9].text()), int(textBoxTable9598[10].text())]
    start9598()
    Results9598.append(p9598.TEXT)


def set_gas_properties():
    Gas.SIM_TIME = int(textBoxTableGas[0].text())
    Gas.GAS_STATION_SIZE = int(textBoxTableGas[1].text())
    Gas.THRESHOLD = int(textBoxTableGas[2].text())
    Gas.NUMBER_OF_PUMP = int(textBoxTableGas[3].text())
    Gas.FUEL_TANK_SIZE = int(textBoxTableGas[4].text())
    Gas.REFUELING_SPEED = int(textBoxTableGas[5].text())
    Gas.TANK_TRUCK_TIME = int(textBoxTableGas[6].text())
    Gas.FUEL_TANK_LEVEL = [int(textBoxTableGas[7].text()), int(textBoxTableGas[8].text())]
    Gas.T_INTER = [int(textBoxTableGas[9].text()), int(textBoxTableGas[10].text())]
    startGas()
    ResultsGas.append(Gas.TEXT)


def set_calculate_button():
    calculateButton.clicked.connect(set_diesel_properties)
    calculateButton.clicked.connect(set_9598_properties)
    calculateButton.clicked.connect(set_gas_properties)
    calculateButton.clicked.connect(NumberOfCarChart.showPlot)


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


def set_form_9598():
    form9598 = QFormLayout()
    form9598.addRow("SIM_TIME", textBoxTable9598[0])
    form9598.addRow("GAS_STATION_SIZE", textBoxTable9598[1])
    form9598.addRow("THRESHOLD [%]", textBoxTable9598[2])
    form9598.addRow("NUMBER_OF_PUMP", textBoxTable9598[3])
    form9598.addRow("FUEL_TANK_SIZE", textBoxTable9598[4])
    form9598.addRow("TANK_TRUCK_TIME", textBoxTable9598[5])
    form9598.addRow("TANK_TRUCK_TIME", textBoxTable9598[6])
    form9598.addRow("FUEL_TANK_LEVEL_MIN", textBoxTable9598[7])
    form9598.addRow("FUEL_TANK_LEVEL_MAX", textBoxTable9598[8])
    form9598.addRow("T_INTER_MIN", textBoxTable9598[9])
    form9598.addRow("T_INTER_MAX", textBoxTable9598[10])
    GroupBoxForm9598.setLayout(form9598)


def set_form_gas():
    formGas = QFormLayout()
    formGas.addRow("SIM_TIME", textBoxTableGas[0])
    formGas.addRow("GAS_STATION_SIZE", textBoxTableGas[1])
    formGas.addRow("THRESHOLD [%]", textBoxTableGas[2])
    formGas.addRow("NUMBER_OF_PUMP", textBoxTableGas[3])
    formGas.addRow("FUEL_TANK_SIZE", textBoxTableGas[4])
    formGas.addRow("TANK_TRUCK_TIME", textBoxTableGas[5])
    formGas.addRow("TANK_TRUCK_TIME", textBoxTableGas[6])
    formGas.addRow("FUEL_TANK_LEVEL_MIN", textBoxTableGas[7])
    formGas.addRow("FUEL_TANK_LEVEL_MAX", textBoxTableGas[8])
    formGas.addRow("T_INTER_MIN", textBoxTableGas[9])
    formGas.addRow("T_INTER_MAX", textBoxTableGas[10])
    GroupBoxFormGas.setLayout(formGas)


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
    set_form_9598()
    set_form_gas()

    set_grid_result_diesel()
    set_grid_result_9598()
    set_grid_result_gas()

    window.setLayout(set_layout_window())
    window.show()


app.exec_()
