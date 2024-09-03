class Celsius:
    def __get__(self, instance, owner):
        return instance._temperature
    
    def __set__(self, instance, value):
        instance._temperature = value

class Temperature:
    celsius = Celsius()

temp = Temperature()
temp.celsius = 25
print(temp.celsius)