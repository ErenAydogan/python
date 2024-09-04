class Deletable:
    def __set__(self, instance, value):
        instance_value = value

    def __get__(self, instance, owner):
        return instance._value
    
    def __delete__(self,instance):
        del instance._value

class MyClass:
    attr = Deletable()

obj = MyClass()
obj.attr = 42
del obj.attr