import Constants as c
import Data as data
import DataFunctions as df
import Classes as c
import colorama
from colorama import Fore, Back, Style
import random


# for diameter 
# 695700km = 1 Solar Radius * 0.621 for miles

if __name__ == "__main__":

    colorama.init(autoreset=True)
    Earth = c.CelestialBody("Earth", 152097597, 147098450, 1, 1, 0)
    Earth.Rand_Object(c.CelestialBody("Moon", 23434938, 8979799, 1, 1, 0))
    Earth.Add_Station(c.Station("Helios"))

    print(f"{Earth.desc()}\n",Earth.Moons[0].desc())
