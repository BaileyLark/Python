# spectral code
# effective tempreture LB 
# effective tempreture UP 
# solar radius LB 
# solar radius UP
# R,G,B
# probability

# Calculates the Solar Radius when given KM
def solarRad(sRad, isKM=True): 
    if(isKM):
        return sRad*695700
    return ((sRad*695700) * 0.621)

Hardvard_spectral_bounds = [
    [79, 30000, 200000, 6.6, 2150, 104, 160, 232, 0.01], # O
    [42, 30000, 10000, 1.8, 6.6, 140, 180, 230, 0.13], # B
    [41, 10000, 7500, 1.4, 1.8, 190, 215, 240, 0.6], # A
    [46, 7500, 6000, 1.15, 1.4, 250, 240, 240, 3], # F
    [47, 6000, 5200, 0.96, 1.15, 250, 217, 203, 7], # G
    [75, 5200, 3700, 0.7, 0.96, 250, 175, 145, 12], # K
    [77, 2400, 3700, 0.17, 0.7, 236, 142, 101, 76], # M 
    ]

# absolute magnitude LB 
# absolute magnitude UB 
# spectral type LB
# spectral type UP
Hertz_class_bounds = [
    [15, 20, 30, 37], # brown dwarf
    [10, 15, 0, 27], # white dwarf
    [0, 7, 4, 30], # main sequence
    [-5, 0, 5, 30], #giants 
    [-11, -6, 8, 30], #hyper giants
]