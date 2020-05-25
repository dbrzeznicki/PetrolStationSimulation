import matplotlib.pyplot as plt

import Diesel
import p9598
import Gas


def showPlot():
    plt.clf()
    plt.plot(Diesel.Plot1SimTime, Diesel.Plot1CarNumber)
    plt.plot(Gas.Plot1SimTime, Gas.Plot1CarNumber)
    plt.plot(p9598.Plot1SimTime, p9598.Plot1CarNumber)

    plt.title('Ilość samochodów - czas')
    plt.xlabel('SIM_TIME')
    plt.ylabel('NUMBER_OF_CAR')
    plt.legend(['Diesel', 'Gas', '9598'], loc=4)
    plt.show()

    Diesel.Plot1SimTime.clear()
    Diesel.Plot1CarNumber.clear()
    Gas.Plot1SimTime.clear()
    Gas.Plot1CarNumber.clear()
    p9598.Plot1SimTime.clear()
    p9598.Plot1CarNumber.clear()
