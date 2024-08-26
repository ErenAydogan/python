class Person:
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi
        if not isinstance(self.name, str):
            raise ValueError("Name value must be a string!")
        if self.age < 0:
            raise ValueError("Age can never be less than zero!")
        if self.bmi < 0:
            raise ValueError("BMI can never be less than zero!")

        
    def __str__(self):
        return "{0} age {1} with a bmi of {2}".format(self.name, self.age,self.bmi)
    

person1 = Person("Josh", 25, 17)
print(person1)