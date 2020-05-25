import matplotlib.pyplot as plt

import Diesel
import p9598
import Gas


def showPlot():
    plt.clf()
    plt.plot(Diesel.Plot2SimTime, Diesel.Plot2Amount)
    plt.plot(Gas.Plot2SimTime, Gas.Plot2Amount)
    plt.plot(p9598.Plot2SimTime, p9598.Plot2Amount)

    plt.title('Ilość zatankowanego paliwa - czas')
    plt.xlabel('SIM_TIME')
    plt.ylabel('AMOUNT_GAS')
    plt.legend(['Diesel', 'Gas', '9598'], loc=4)
    plt.show()

    Diesel.Plot2SimTime.clear()
    Diesel.Plot2Amount.clear()
    Gas.Plot2SimTime.clear()
    Gas.Plot2Amount.clear()
    p9598.Plot2SimTime.clear()
    p9598.Plot2Amount.clear()
