import matplotlib.pyplot as plt

import Diesel
import p9598
import Gas


def showPlot():
    plt.clf()
    plt.bar('Gas', Gas.TANK_TRUCK_COUNT, label='Gas')
    plt.bar('9598', p9598.TANK_TRUCK_COUNT, label='9598')
    plt.bar('Diesel', Diesel.TANK_TRUCK_COUNT, label='Diesel')
    plt.legend()
    plt.xlabel('Rodzaj paliwa')
    plt.ylabel('Liczba dostaw paliwa')
    plt.title('Liczba dostaw danego paliwa')
    plt.show()
    Diesel.TANK_TRUCK_COUNT = 0
    p9598.TANK_TRUCK_COUNT = 0
    Gas.TANK_TRUCK_COUNT = 0
