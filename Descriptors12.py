class ListDescriptor:
    def __get__(self, instance, owner):
        return instance._list
    
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("It must be a list")
        
        instance._list = value

class MyClass:
    myList = ListDescriptor()

obj = MyClass()
obj.myList = [1,2,3]
print(obj.myList)
