import Constants as c
import Data as data
import DataFunctions as df
import Classes as c
import random

# for diameter 
# 695700km = 1 Solar Radius * 0.621 for miles

if __name__ == "__main__":
    Earth = c.CelestialBody("Earth", 152097597, 147098450, 1, 1, 0)
    Earth.Rand_Add_Object(c.CelestialBody("Moon", 23434938, 8979799, 1, 1, 0))
    print(f"{Earth.desc()}\n",Earth.Moons[0].desc())
    #print(f"{Earth.Moons[0].Object_type}")