class UpperCaseDescriptor:
    def __get__(self, instance, owner):
        return instance._text.upper()
    
    def __set__(self, instance, value):
        instance._text = value

class MyClass:
    text = UpperCaseDescriptor()


obj = MyClass()
obj.text = "Hello World"
print(obj.text)