class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print("Getting Name")
        return self._name
    
    def setName(self, name):
        print("Setting the name to :", name)
        self._name = name

    def delName(self):
        print("Deleting the name")
        del self._name

    name = property(getName, setName, delName)


name = Person("John") 
print(name.name)
name.name = "Price"
del name.name