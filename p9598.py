"""
Gas Station Refueling example

Covers:

- Resources: Resource
- Resources: Container
- Waiting for other processes

Scenario:
  A gas station has a limited number of gas pumps that share a common
  fuel reservoir. Cars randomly arrive at the gas station, request one
  of the fuel pumps and start refueling from that reservoir.

  A gas station control process observes the gas station's fuel level
  and calls a tank truck for refueling if the station's level drops
  below a threshold.

"""
import itertools
import random
import simpy
from datetime import datetime

SIM_TIME = 10000  # Simulation time in seconds
GAS_STATION_SIZE = 2000  # liters
THRESHOLD = 10  # Threshold for calling the tank truck (in %)

NUMBER_OF_PUMP = 2
FUEL_TANK_SIZE = 50  # liters
REFUELING_SPEED = 2  # liters / second
TANK_TRUCK_TIME = 300  # Seconds it takes the tank truck to arrive

FUEL_TANK_LEVEL = [5, 25]  # Min/max levels of fuel tanks (in liters)
T_INTER = [10, 30]  # Create a car every [min, max] seconds

TEXT = ""
AMOUNT_OF_FUEL_REFUELED = 0


def car(name, env, gas_station, fuel_pump):
    """A car arrives at the gas station for refueling.

    It requests one of the gas station's fuel pumps and tries to get the
    desired amount of gas from it. If the stations reservoir is
    depleted, the car has to wait for the tank truck to arrive.

    """
    fuel_tank_level = random.randint(*FUEL_TANK_LEVEL)
    global AMOUNT_OF_FUEL_REFUELED
    AMOUNT_OF_FUEL_REFUELED += fuel_tank_level
    global TEXT
    TEXT += '%s arriving at gas station at %.1f \n' % (name, env.now)
    with gas_station.request() as req:
        start = env.now
        # Request one of the gas pumps
        yield req

        # Get the required amount of fuel
        liters_required = FUEL_TANK_SIZE - fuel_tank_level
        yield fuel_pump.get(liters_required)

        # The "actual" refueling process takes some time
        yield env.timeout(liters_required / REFUELING_SPEED)

        TEXT += '%s finished refueling in %.1f seconds. \n' % (name, env.now - start)


def gas_station_control(env, fuel_pump):
    """Periodically check the level of the *fuel_pump* and call the tank
    truck if the level falls below a threshold."""
    while True:
        if fuel_pump.level / fuel_pump.capacity * 100 < THRESHOLD:
            # We need to call the tank truck now!
            global TEXT
            TEXT += 'Calling tank truck at %d \n' % env.now
            # Wait for the tank truck to arrive and refuel the station
            yield env.process(tank_truck(env, fuel_pump))

        yield env.timeout(10)  # Check every 10 seconds


def tank_truck(env, fuel_pump):
    """Arrives at the gas station after a certain delay and refuels it."""
    yield env.timeout(TANK_TRUCK_TIME)
    global TEXT
    TEXT += 'Tank truck arriving at time %d \n' % env.now
    ammount = fuel_pump.capacity - fuel_pump.level
    TEXT += 'Tank truck refuelling %.1f liters. \n' % ammount
    yield fuel_pump.put(ammount)


def car_generator(env, gas_station, fuel_pump):
    """Generate new cars that arrive at the gas station."""
    for i in itertools.count():
        yield env.timeout(random.randint(*T_INTER))
        env.process(car('Car %d' % i, env, gas_station, fuel_pump))


def start9598():
    # Setup and start the simulation
    global TEXT
    TEXT = 'Gas Station refuelling\n'
    random.seed(datetime.now())

    # Create environment and start processes
    env = simpy.Environment()
    gas_station = simpy.Resource(env, NUMBER_OF_PUMP)
    fuel_pump = simpy.Container(env, GAS_STATION_SIZE, init=GAS_STATION_SIZE)
    env.process(gas_station_control(env, fuel_pump))
    env.process(car_generator(env, gas_station, fuel_pump))

    # Execute!
    env.run(until=SIM_TIME)