import Constants as c
import Data as data
import DataFunctions as df
import Classes as c
import random

# for diameter 
# 695700km = 1 Solar Radius * 0.621 for miles

if __name__ == "__main__":
    p001 = c.CelestialBody("Earth", 152097597, 147098450)
    p001.addOrbitingBody(c.CelestialBody("Moon", 405550, 226000, 1, 1, 1))
    print("\n" + p001.description())
    print(p001.Moons[0].description())
    print(p001.Moons[0].OrbitingBody.Name)
    