# spectral code
# effective tempreture LB 
# effective tempreture UP 
# solar radius LB 
# solar radius UP
# R,G,B
# probability
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

# Celestial (km) Collective (ly)
# radius LB 
# radius UB
# n/a

Object_Types = [
    ["Terrestrial", 2439, 38226, 0], 
    ["Gas Giant", 10842, 174777, 0],
    ["Natural Satalite", 400, 2439, 0],
    ["Spiral Galaxy", 100000, 500000, 0]
    ["Elliptical Galaxy", 500, 25000, 0]
    ["Barred Galaxy", 75000, 150000]
    ["Irregular Galaxy", 25000, 75000]
]

'''Objecs_Types = [
    ["White Dwarf"],
    ["Main Sequence"],
    ["Gaints"],
    ["Hyper Giants"],
    ["Black Hole"],
    ["Neutron Star"],
    ["Quasar"],
    ["Terrestrial"], 
    ["Natural Satalite"], 
    ["Gas Giant"],
    ["Galaxy", 200, 500000, 0]
]'''

