class Person:
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        #return "{0} age {1} with a bmi of {2}".format(self.name, self.age, self.bmi)
        return f"{self.name} age {self.age} with a bmi of {self.bmi}"
    

person1 = Person("Joe", 21, 17)
print(person1)