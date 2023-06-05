import Constants as c
import Data as data
import DataFunctions as df
import Classes as c
import colorama
from colorama import Fore, Back, Style
import random
import json
import tkinter as tk 

#root = tk.Tk()
#entry = tk.Entry(root, width=10).pack()

if __name__ == "__main__":
    Player1 = c.PlayerInfo()
    print(Player1.Starship.Storage[0].Rarity)


    #root.mainloop()

# Have player enter their name


    #data = json.load(open('save.json')) # imports json, then converts it into dictionary
    #print(data['current_save'][0]['name']) #
    #Player1 = c.PlayerInfo()
    #colorama.init(autoreset=True)
    #Earth = c.CelestialBody("Earth", 152097597, 147098450, 1, 1, 0)
    #Earth.Rand_Object(c.CelestialBody("Moon", 23434938, 8979799, 1, 1, 0))
    #Earth.Add_Station(c.Station("Helios"))
    #print(f"{Earth.desc()}")