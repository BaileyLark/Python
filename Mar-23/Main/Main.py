import Constants as c
import Data as data
import DataFunctions as df
import Classes as c
import colorama
from colorama import Fore, Back, Style
import random
import json


# for diameter 
# 695700km = 1 Solar Radius * 0.621 for miles

if __name__ == "__main__":

    #data = json.load(open('save.json')) # imports json, then converts it into dictionary
    #print(data['current_save'][0]['name']) #
    Player1 = c.PlayerInfo()
    print(Player1.Starship.Storage[0])
    #colorama.init(autoreset=True)
    Earth = c.CelestialBody("Earth", 152097597, 147098450, 1, 1, 0)
    Earth.Rand_Object(c.CelestialBody("Moon", 23434938, 8979799, 1, 1, 0))
    Earth.Add_Station(c.Station("Helios"))
    print(f"{Earth.desc()}")

# Have player enter their name