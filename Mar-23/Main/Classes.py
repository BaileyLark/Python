import DataFunctions as df
import Data as data
import random 
import colorama
from colorama import Fore, Back, Style

# PLAYER INFO

class PlayerInfo(): 
    def __init__(self):
        self.CommmanderName = ""
        self.Frakts = 100 
        self.Starship = Starship()
        self.CurrentSystem = None 

class Starship():
    Storage = [] 
    Storage_Cap = 50

# ITEM SHOP/EXCHANGE

class Station():
    def __init__(self, name:str):
        self.Name = name
        self.Storage = []
        self.OrbitingBody = None
    def __str__(self):
        return f"{self.Name}, Orbiting: {self.OrbitingBody.Name}"


# UNIVERSE

# decide if objects should be seperate lists, speeding up sorting
Universe = []

class GalaxyContainer:
    Systems = []

class SystemContainer:
    def __init__(self, Name:str, Radius=1, Randbodies=0, Object_type=5):
        Universe.append(self)
        self.CelestialBodies = []

class CelestialBody():
    def __init__(self, Name:str, Aphelion: int, Perihelion: int, Radius=1, invariablePlane=1, Object_type=0, orbitingBody=None):

        Universe.append(self)

        #IDENTIFICATION
        self.Name = Name # Needs specific function to generate name
        self.Object_type = data.Object_Types[Object_type][0]
        
        #ORBITAL
        self.Aphelion = Aphelion
        self.Perihelion = Perihelion
        self.Eccentricity = df.calcEccentricity(self.Aphelion, self.Perihelion)  
        self.OrbitingBody = orbitingBody
        self.invariablePlane = invariablePlane 
        if (self.invariablePlane):
            self.invariablePlane = round(random.uniform(0,10), 7) # Needs gaussian distribution

        #MASS
        self.Radius = Radius
        if (Radius):
            self.Radius = round(random.uniform(data.Object_Types[Object_type][1], data.Object_Types[Object_type][2]))

        #ORBITING BODIES / REFERENCE
        self.System = None
        self.Moons = []
        self.Station = None

    def Rand_Object(self, object):
        self.Moons.append(object)
        object.Object_type = data.Object_Types[2][0]
        object.Radius = round(random.uniform(500, self.Radius * 0.7))
        object.Aphelion = self.Aphelion + object.Aphelion
        object.Perihelion = self.Perihelion - object.Perihelion
        object.OrbitingBody = self

    def Add_Station(self, object):
        self.Station = object
        self.Station.OrbitingBody = self

    def desc(self): # Testing purposes
        text = ""
        text += f"{self.Name} ({self.Object_type})\n"
        if (not(self.Object_type == "Natural Satalite")):
            text += f"Aphelion: {self.Aphelion:,}km \nPerihelion: {self.Perihelion:,}km \nEccentricity {self.Eccentricity:,}\n"
        else:
            text += f"Apogee: {self.Aphelion:,}km ({self.Aphelion - self.OrbitingBody.Aphelion:,}km) \
            \nPerigee: {self.Perihelion:,}km ({self.OrbitingBody.Perihelion - self.Perihelion:,}km) \
            \nEccentricity {self.Eccentricity:,}\n"
        text += f"invariablePlane: {self.invariablePlane}\n"
        text += f"Radius: {self.Radius}km\n" 
        text += f"Moons: {len(self.Moons)}\n" 
        text += f"Parent: {self.OrbitingBody}\n"
        return text
    
    # Add Fore.COLOR to each string for it to work

'''
class Item():
    def __init__(self, name:str, stack:int, desc:str):
        self.Name = name 
        self.Stack = stack
        self.Description = desc
'''

        

