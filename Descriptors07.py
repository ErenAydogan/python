class RangeDescriptor:
    def __init__(self, name=None, min_value=0, max_value=100):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, self.min_value)
    
    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError("{0} must be between {1} and {2}".format(self.name, self.min_value, self.max_value))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Product:
    price = RangeDescriptor(name="price", min_value=10, max_value=1000)


item = Product()
item.price = 200
print(item.price)
        