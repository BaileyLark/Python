import DataFunctions as df
import Data as data
import random 


Universe = []

class PlayerInfo: 
    Frakts = 100 

class Item():
    def __init__(self, name:str, stack:int, desc:str):
        self.Name = name 
        self.Stack = stack
        self.Description = desc

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

    def Rand_Add_Object(self, object):
        self.Moons.append(object)
        object.Object_type = data.Object_Types[2][0]
        object.Radius = round(random.uniform(500, self.Radius * 0.7))
        object.Aphelion = self.Aphelion + object.Aphelion
        object.Perihelion = self.Perihelion - object.Perihelion
        object.OrbitingBody = self

    def desc(self): # Testing purposes
        text = ""
        text = f"{self.Name} ({self.Object_type})\n"
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




        

