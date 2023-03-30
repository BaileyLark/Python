import Constants as c
import Data as data
import DataFunctions as df
import Classes as c
import random

# for diameter 
# 695700km = 1 Solar Radius * 0.621 for miles

if __name__ == "__main__":
    System = c.SystemContainer()
    System.Add_CeleBody(c.CelestialBody("Earth", 152097597, 147098450, 1, 1, 0))
    print(System.CelestialBodies[0])
    