class PositiveNumber:
    def __init__(self, number):
        self._number = number

    def setNumber(self, number):
        if number < 0:
            raise ValueError("The value cannot be less than 0")
        self._number = number

    def getNumber(self):
        return self._number

    number = property(getNumber, setNumber)

obj = PositiveNumber(10)
print(obj.number)
