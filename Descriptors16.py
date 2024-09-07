class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    def getTemperature(self):
        return self._temperature
    
    def setTemperature(self, temperature):
        self._temperature = temperature

    Celsius = property(getTemperature, setTemperature)

temp = Celsius(25)
print(temp.Celsius)