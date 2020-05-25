import matplotlib.pyplot as plt

import Diesel
import p9598
import Gas


def showPlot():
    plt.clf()
    plt.bar('Gas', Gas.AMOUNT_OF_FUEL_REFUELED, label='Gas')
    plt.bar('9598', p9598.AMOUNT_OF_FUEL_REFUELED, label='9598')
    plt.bar('Diesel', Diesel.AMOUNT_OF_FUEL_REFUELED, label='Diesel')
    plt.legend()
    plt.xlabel('Rodzaj paliwa')
    plt.ylabel('Ilość paliwa [l]')
    plt.title('Ilość zatankowanego paliwa danego rodzaju')
    plt.show()
    Diesel.AMOUNT_OF_FUEL_REFUELED = 0
    p9598.AMOUNT_OF_FUEL_REFUELED = 0
    Gas.AMOUNT_OF_FUEL_REFUELED = 0
