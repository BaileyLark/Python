class Car:

    perf_upgrade = 1.03 # class variable Car.perf_upgrade = 5

    def __init__(self, model, cost, horsepower): # init = initialization  
        self.model = model
        self.cost = cost 
        self.horsepower = horsepower

    def display(self): # must always have self 
        return f'{self.model}, {self.cost}, {self.horsepower}'

    def upgrade(self):
        horsepower *= self.perf_upgrade 
        # the variable has to accessed through a class instance




def main():
    vehicle = Car('Ferrari', '1000000' , 750)
    vehicle.spolier = True # instance variable
    print(vehicle.display())




if __name__ == "__main__":
    main()