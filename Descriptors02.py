class Descriptors:
    def __init__(self):
        self.__bmi = 0
    def __get__(self, instance, owner):
        return self.__bmi
    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)

        else:
            raise TypeError("BMI must be an integer")
        
        if value<0:
            raise ValueError("BMI cannot be less then zero")
        

        self. __bmi = value
    
    def __delete__(self, instance):
        del self.__bmi


class Person:
    bmi = Descriptors()
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        return "{0} age is {1} and his bmi is {2}".format(self.name, self.age, self.bmi)
    
person1 = Person("John", 20, "10")
print(person1)