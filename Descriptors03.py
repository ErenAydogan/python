class PositiveNumber:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("The value cannot be less than 0")
        instance._value=value


    def __get__(self, instance, owner):
        return instance._value
    
class MyClass:
    number = PositiveNumber()

obj = MyClass()
obj.number = 10
print(obj.number)