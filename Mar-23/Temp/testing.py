car = {
    "brand":"Ferrari", 
    "speed":"210", 
    "horsepower":"700", 
    "year":"1995", 
}

vehicles = [
    {
    "brand":"Porsche", 
    "speed":"195", 
    "horsepower":"650", 
    "year":"2005", 
    }, 
    {
    "brand":"Lamborghini", 
    "speed":"215", 
    "horsepower":"750", 
    "year":"2003", 
    }, 
]

#for i in range(1, 10, 2): # the 2 is the multiples (steps)


for index, item in enumerate(car): # emumerate returns index and item
    print(index, item)