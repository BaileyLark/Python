from msilib.schema import Class
import DataFunctions as df
import Data as data
import random 

class GalaxyContainer:
    Systems = []

class SystemContainer:
    CelestialBody = []

class CelestialBody():

    def __init__(self, Name:str, Aphelion: int, Perihelion: int, Radius=1, invariablePlane=1, Object_type=0):

        #IDENTIFICATION
        self.Name = Name # Needs specific function to generate name
        self.Object_type = data.Object_Types[Object_type][0]

        #ORBITAL
        self.Aphelion = Aphelion
        self.Perihelion = Perihelion
        self.Eccentricity = df.calcEccentricity(self.Aphelion, self.Perihelion)  
        self.OrbitingBody = 0
        self.invariablePlane=invariablePlane 
        if (self.invariablePlane):
            self.invariablePlane = round(random.uniform(0,10), 7) # Needs gaussian distribution

        #MASS
        self.Radius = Radius
        if (Radius):
            self.Radius = round(random.uniform(data.Object_Types[Object_type][1], data.Object_Types[Object_type][2]))

        #ORBITING BODIES
        self.Moons = [] 
    

    def addOrbitingBody(self, MoonClass):
        self.Moons.append(MoonClass)
        MoonClass.Object_type = data.Object_Types[2][0]
        MoonClass.Radius = round(random.uniform(500, self.Radius * 0.7))
        MoonClass.Aphelion = self.Aphelion + MoonClass.Aphelion
        MoonClass.Perihelion = self.Perihelion - MoonClass.Perihelion


    def remOrbitingBody(self, index):
        if (self.Moons[index]):
            self.Moons.pop(index)

    def testing(self):
        print("hello")

    def __str__(self):
        return f"\n{self.Name} ({self.Object_type}) \
        \nAphelion: {self.Aphelion:,}km \
        \nPerihelion: {self.Perihelion:,}km \nEccentricity {self.Eccentricity:,} \
        \ninvariablePlane: {self.invariablePlane} \
        \nRadius: {self.Radius}km \
        \nMoons: {len(self.Moons)} \n"


