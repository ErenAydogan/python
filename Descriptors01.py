class MyDescriptor:
    def __get__(self, instance, owner): 
        return "Bu bir descriptor."

class MyClass:
    descriptor = MyDescriptor()

obj = MyClass() #instance is the variable "obj". #owner is the class "MyClass" 
print(obj.descriptor)