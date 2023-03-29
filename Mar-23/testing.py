class Object():

    def __init__(self, Name):
        self.name = Name
        self.classInstances = []
    
    def appendClass(self, objectInstance):
        self.classInstances.append(objectInstance)
    
    def printName(self):
        print(self.name)

if __name__ == "__main__":
    Parent = Object("Parent")
    Parent.appendClass(Object("Child"))
    Parent.classInstances[0].printName()


