from scipy.stats import truncnorm
import itertools
import random
import simpy
from datetime import datetime

SIM_TIME = 10000
GAS_STATION_SIZE = 2000
THRESHOLD = 10
NUMBER_OF_PUMP = 2
REFUELING_SPEED = 2
TANK_TRUCK_TIME = 300
FUEL_TANK_LEVEL = [5, 25]
T_INTER = [10, 30]

TEXT = ""
AMOUNT_OF_FUEL_REFUELED = 0
TANK_TRUCK_COUNT = 0
CHOICE = 1
Plot1SimTime = []
Plot1CarNumber = []
Plot2SimTime = []
Plot2Amount = []


def car(name, env, gas_station, fuel_pump):

    if CHOICE == 0:
        fuel_tank_level = random.randint(*FUEL_TANK_LEVEL)
    elif CHOICE == 1:
        tmpMean = (FUEL_TANK_LEVEL[0] + FUEL_TANK_LEVEL[1])/2
        X = get_truncated_normal(mean=tmpMean, sd=1, low=FUEL_TANK_LEVEL[0], upp=FUEL_TANK_LEVEL[1])
        fuel_tank_level = int(X.rvs())

    global AMOUNT_OF_FUEL_REFUELED
    AMOUNT_OF_FUEL_REFUELED += fuel_tank_level

    global TEXT
    TEXT += '%s arriving at gas station at %.1f \n' % (name, env.now)
    Plot1SimTime.append(env.now)
    with gas_station.request() as req:
        start = env.now
        yield req
        yield fuel_pump.get(fuel_tank_level)
        yield env.timeout(fuel_tank_level / REFUELING_SPEED)
        TEXT += '%s finished refueling in %.1f seconds. \n' % (name, env.now - start)
        Plot2SimTime.append(env.now)
        Plot2Amount.append(AMOUNT_OF_FUEL_REFUELED)


def gas_station_control(env, fuel_pump):
    while True:
        if fuel_pump.level / fuel_pump.capacity * 100 < THRESHOLD:
            global TEXT
            TEXT += 'Calling tank truck at %d \n' % env.now
            yield env.process(tank_truck(env, fuel_pump))
        yield env.timeout(10)


def tank_truck(env, fuel_pump):
    yield env.timeout(TANK_TRUCK_TIME)
    global TEXT
    TEXT += 'Tank truck arriving at time %d \n' % env.now
    ammount = fuel_pump.capacity - fuel_pump.level
    TEXT += 'Tank truck refuelling %.1f liters. \n' % ammount
    global TANK_TRUCK_COUNT
    TANK_TRUCK_COUNT += 1
    yield fuel_pump.put(ammount)


def car_generator(env, gas_station, fuel_pump):
    for i in itertools.count():
        if CHOICE == 0:
            tmp = random.randint(*T_INTER)
        elif CHOICE == 1:
            tmpMean = (T_INTER[0] + T_INTER[1]) / 2
            X = get_truncated_normal(mean=tmpMean, sd=1, low=T_INTER[0], upp=T_INTER[1])
            tmp = int(X.rvs())
        yield env.timeout(tmp)
        env.process(car('Car %d' % i, env, gas_station, fuel_pump))
        Plot1CarNumber.append(i)


def startDiesel():
    global TEXT
    TEXT = 'Gas Station refuelling\n'
    random.seed(datetime.now())

    env = simpy.Environment()
    gas_station = simpy.Resource(env, NUMBER_OF_PUMP)
    fuel_pump = simpy.Container(env, GAS_STATION_SIZE, init=GAS_STATION_SIZE)
    env.process(gas_station_control(env, fuel_pump))
    env.process(car_generator(env, gas_station, fuel_pump))

    env.run(until=SIM_TIME)


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
