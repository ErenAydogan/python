class StringDescriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, "")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("{0} must be a string".format(self.name))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person:
    name = StringDescriptor("name")


p = Person()
p.name = "Joe"
print(p.name)