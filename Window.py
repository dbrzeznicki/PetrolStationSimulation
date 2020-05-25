import sys

from PySide2.QtWidgets import*

import Diesel
from Diesel import startDiesel

import p9598
from p9598 import start9598

import Gas
from Gas import startGas

import RefuelingCountChart
import NumberOfCarTimeChart
import AmountTimeChart
import TankTruckArrivingChart


app = QApplication(sys.argv)

textBoxTableDiesel = [QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"),
                      QLineEdit("2"), QLineEdit("30"), QLineEdit("5"), QLineEdit("25"), QLineEdit("10"),
                      QLineEdit("30")]

textBoxTable9598 = [QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"),
                    QLineEdit("2"), QLineEdit("30"), QLineEdit("5"), QLineEdit("25"), QLineEdit("10"),
                    QLineEdit("30")]

textBoxTableGas = [QLineEdit("2000"), QLineEdit("10"), QLineEdit("2"),
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

GroupBoxTop = QGroupBox("Basic information")
TopLabelSimTime = QLabel("SIM_TIME")
ProbabilityDistribution = QLabel("PROBABILITY_DISTRIBUTION")
SIM_TIME_LINE_EDIT = QLineEdit("10000")
ComboBoxProbability = QComboBox()


def set_combo_box():
    ComboBoxProbability.addItem("Random")
    ComboBoxProbability.addItem("NormalDistribution")


def set_diesel_properties():
    Diesel.SIM_TIME = int(SIM_TIME_LINE_EDIT.text())
    Diesel.GAS_STATION_SIZE = int(textBoxTableDiesel[0].text())
    Diesel.THRESHOLD = int(textBoxTableDiesel[1].text())
    Diesel.NUMBER_OF_PUMP = int(textBoxTableDiesel[2].text())
    Diesel.REFUELING_SPEED = int(textBoxTableDiesel[3].text())
    Diesel.TANK_TRUCK_TIME = int(textBoxTableDiesel[4].text())
    Diesel.FUEL_TANK_LEVEL = [int(textBoxTableDiesel[5].text()), int(textBoxTableDiesel[6].text())]
    Diesel.T_INTER = [int(textBoxTableDiesel[7].text()), int(textBoxTableDiesel[8].text())]
    if ComboBoxProbability.currentIndex() == 0:
        Diesel.CHOICE = 0
    elif ComboBoxProbability.currentIndex() == 1:
        Diesel.CHOICE = 1

    startDiesel()
    ResultsDiesel.append(Diesel.TEXT)


def set_9598_properties():
    p9598.SIM_TIME = int(SIM_TIME_LINE_EDIT.text())
    p9598.GAS_STATION_SIZE = int(textBoxTable9598[0].text())
    p9598.THRESHOLD = int(textBoxTable9598[1].text())
    p9598.NUMBER_OF_PUMP = int(textBoxTable9598[2].text())
    p9598.REFUELING_SPEED = int(textBoxTable9598[3].text())
    p9598.TANK_TRUCK_TIME = int(textBoxTable9598[4].text())
    p9598.FUEL_TANK_LEVEL = [int(textBoxTable9598[5].text()), int(textBoxTable9598[6].text())]
    p9598.T_INTER = [int(textBoxTable9598[7].text()), int(textBoxTable9598[8].text())]
    if ComboBoxProbability.currentIndex() == 0:
        p9598.CHOICE = 0
    elif ComboBoxProbability.currentIndex() == 1:
        p9598.CHOICE = 1
    start9598()
    Results9598.append(p9598.TEXT)


def set_gas_properties():
    Gas.SIM_TIME = int(SIM_TIME_LINE_EDIT.text())
    Gas.GAS_STATION_SIZE = int(textBoxTableGas[0].text())
    Gas.THRESHOLD = int(textBoxTableGas[1].text())
    Gas.NUMBER_OF_PUMP = int(textBoxTableGas[2].text())
    Gas.REFUELING_SPEED = int(textBoxTableGas[3].text())
    Gas.TANK_TRUCK_TIME = int(textBoxTableGas[4].text())
    Gas.FUEL_TANK_LEVEL = [int(textBoxTableGas[5].text()), int(textBoxTableGas[6].text())]
    Gas.T_INTER = [int(textBoxTableGas[7].text()), int(textBoxTableGas[8].text())]
    if ComboBoxProbability.currentIndex() == 0:
        Gas.CHOICE = 0
    elif ComboBoxProbability.currentIndex() == 1:
        Gas.CHOICE = 1
    startGas()
    ResultsGas.append(Gas.TEXT)


def set_calculate_button():
    calculateButton.clicked.connect(set_diesel_properties)
    calculateButton.clicked.connect(set_9598_properties)
    calculateButton.clicked.connect(set_gas_properties)
    calculateButton.clicked.connect(RefuelingCountChart.showPlot)
    calculateButton.clicked.connect(NumberOfCarTimeChart.showPlot)
    calculateButton.clicked.connect(AmountTimeChart.showPlot)
    calculateButton.clicked.connect(TankTruckArrivingChart.showPlot)


def set_form_diesel():
    formDiesel = QFormLayout()
    formDiesel.addRow("GAS_STATION_SIZE", textBoxTableDiesel[0])
    formDiesel.addRow("THRESHOLD [%]", textBoxTableDiesel[1])
    formDiesel.addRow("NUMBER_OF_PUMP", textBoxTableDiesel[2])
    formDiesel.addRow("TANK_TRUCK_TIME", textBoxTableDiesel[3])
    formDiesel.addRow("TANK_TRUCK_TIME", textBoxTableDiesel[4])
    formDiesel.addRow("FUEL_TANK_LEVEL_MIN", textBoxTableDiesel[5])
    formDiesel.addRow("FUEL_TANK_LEVEL_MAX", textBoxTableDiesel[6])
    formDiesel.addRow("T_INTER_MIN", textBoxTableDiesel[7])
    formDiesel.addRow("T_INTER_MAX", textBoxTableDiesel[8])
    GroupBoxFormDiesel.setLayout(formDiesel)


def set_form_9598():
    form9598 = QFormLayout()
    form9598.addRow("GAS_STATION_SIZE", textBoxTable9598[0])
    form9598.addRow("THRESHOLD [%]", textBoxTable9598[1])
    form9598.addRow("NUMBER_OF_PUMP", textBoxTable9598[2])
    form9598.addRow("TANK_TRUCK_TIME", textBoxTable9598[3])
    form9598.addRow("TANK_TRUCK_TIME", textBoxTable9598[4])
    form9598.addRow("FUEL_TANK_LEVEL_MIN", textBoxTable9598[5])
    form9598.addRow("FUEL_TANK_LEVEL_MAX", textBoxTable9598[6])
    form9598.addRow("T_INTER_MIN", textBoxTable9598[7])
    form9598.addRow("T_INTER_MAX", textBoxTable9598[8])
    GroupBoxForm9598.setLayout(form9598)


def set_form_gas():
    formGas = QFormLayout()
    formGas.addRow("GAS_STATION_SIZE", textBoxTableGas[0])
    formGas.addRow("THRESHOLD [%]", textBoxTableGas[1])
    formGas.addRow("NUMBER_OF_PUMP", textBoxTableGas[2])
    formGas.addRow("TANK_TRUCK_TIME", textBoxTableGas[3])
    formGas.addRow("TANK_TRUCK_TIME", textBoxTableGas[4])
    formGas.addRow("FUEL_TANK_LEVEL_MIN", textBoxTableGas[5])
    formGas.addRow("FUEL_TANK_LEVEL_MAX", textBoxTableGas[6])
    formGas.addRow("T_INTER_MIN", textBoxTableGas[7])
    formGas.addRow("T_INTER_MAX", textBoxTableGas[8])
    GroupBoxFormGas.setLayout(formGas)


def set_form_basic_information():
    formBasicInformation = QGridLayout()
    set_combo_box()
    formBasicInformation.addWidget(TopLabelSimTime, 0, 0)
    formBasicInformation.addWidget(SIM_TIME_LINE_EDIT, 0, 1)
    formBasicInformation.addWidget(ProbabilityDistribution, 0, 2)
    formBasicInformation.addWidget(ComboBoxProbability, 0, 3)
    GroupBoxTop.setLayout(formBasicInformation)


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
    layoutWindow.addWidget(GroupBoxTop, 0, 0, 1, 3)
    layoutWindow.addWidget(GroupBoxFormDiesel, 1, 0)
    layoutWindow.addWidget(GroupBoxForm9598, 1, 1)
    layoutWindow.addWidget(GroupBoxFormGas, 1, 2)
    layoutWindow.addWidget(calculateButton, 2, 0, 1, 3)
    layoutWindow.addWidget(GroupBoxResultsDiesel, 3, 0)
    layoutWindow.addWidget(GroupBoxResults9598, 3, 1)
    layoutWindow.addWidget(GroupBoxResultsGas, 3, 2)
    return layoutWindow


class Window:
    window = QWidget()
    set_calculate_button()

    set_form_basic_information()
    set_form_diesel()
    set_form_9598()
    set_form_gas()

    set_grid_result_diesel()
    set_grid_result_9598()
    set_grid_result_gas()

    window.setLayout(set_layout_window())
    window.show()


app.exec_()
