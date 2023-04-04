# Calculates the Solar Radius when given KM

def solarRad(sRad, isKM=True): 
    if(isKM):
        return sRad*695700
    return ((sRad*695700) * 0.621)

# Calculates Eccentricity of an object
def calcEccentricity(Aphelion, Perihelion):
    a, p = float(Aphelion), float(Perihelion)
    return round((a - p) / (a + p), 7)

# generate name of planets
def genName():
    ...
