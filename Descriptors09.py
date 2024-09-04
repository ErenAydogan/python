class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class MyClass:
    x = Descriptor("x")
    y = Descriptor("y")

obj = MyClass()
obj.x = 10
obj.y = 20
print(obj.x, obj.y)