import DataFunctions as df
import Data as data
import random 

class ObjectList: # All objects in the Universe 
    ...
class PlayerInfo: 
    ...

class GalaxyContainer:
    Systems = []

class SystemContainer:
    def __init__(self, Name:str, Radius=1, Randbodies=0, Object_type=5):
        CelestialBodies = []
        self.Object_type = data.Object_Types[3]
        if (Randbodies>0):
            for i in range(Randbodies):
                self.Add_RandCeleBody()

    def Add_CeleBody(self, CelestialClass):
        self.CelestialBodies.append(CelestialClass)
        CelestialClass.System = self
    
    def Add_RandCeleBody():
        ...

class CelestialBody():

    def __init__(self, Name:str, Aphelion: int, Perihelion: int, Radius=1, invariablePlane=1, Object_type=0, orbitingBody=None):

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
        self.Moons = [] 
        self.System = None
    
    def addOrbitingBody(self, MoonClass):
        self.Moons.append(MoonClass)
        MoonClass.Object_type = data.Object_Types[2][0]
        MoonClass.Radius = round(random.uniform(500, self.Radius * 0.7))
        MoonClass.Aphelion = self.Aphelion + MoonClass.Aphelion
        MoonClass.Perihelion = self.Perihelion - MoonClass.Perihelion
        MoonClass.OrbitingBody = self

    def remOrbitingBody(self, index):
        if (self.Moons[index]):
            self.Moons.pop(index)

    def description(self): # Testing purposes
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



        

