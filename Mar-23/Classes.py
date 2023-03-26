from pickle import NONE
import DataFunctions as df
import random 



class GalaxyContainer:
    Systems = []

class SystemContainer:
    CelestialBody = []

class CelestialBody():
    def __init__(self, Name:str, Aphelion: int, Perihelion: int, Radius=1, invariablePlane=1):

        #IDENTIFICATION
        self.Name = Name # Needs specific function to generate name
        self.Classification = ""

        #ORBITAL
        self.Aphelion = Aphelion
        self.Perihelion = Perihelion
        self.Eccentricity = df.calcEccentricity(self.Aphelion, self.Perihelion)  
        self.OrbitingBody = NONE
        self.invariablePlane=invariablePlane 
        if (self.invariablePlane):
            self.invariablePlane = round(random.uniform(0,10), 7) # Needs gaussian distribution

        #MASS
        self.Radius = Radius
        if (Radius):
            self.Radius = round(random.uniform(550,172775))

        #ORBITING BODIES
        self.Moons = [] 
    
    def addOrbitingBody():
        ...

    def remOrbitingBody():
        ...




    def __str__(self):
        return f"{self.Name} \nAphelion: {self.Aphelion:,}km \
        \nPerihelion: {self.Perihelion:,}km \nEccentricity {self.Eccentricity:,} \
        \ninvariablePlane: {self.invariablePlane} \
        \nRadius: {self.Radius}km"
        


