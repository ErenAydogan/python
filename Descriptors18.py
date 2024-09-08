class Person:
    def __init__(self, name=None):
        self.setName(name)

    def getName(self):
        return self._name
    def setName(self, name):
        if not isinstance(name, str):
            raise ValueError("{0} must be a string".format(name))
        self._name = name

    def delName(self):
        del self._name

    name = property(getName, setName, delName)

p = Person(22)
print(p.name)
