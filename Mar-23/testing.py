

class Child():
    def __init__(self):
        self.objects = []
    def add_item(self, i):
        self.objects.append(i)

class Parent(Child):
    ...

if __name__ == "__main__":
    Obj1 = Parent()
    Parent.add_item(Parent, 5)
    print(Obj1.list[0])
