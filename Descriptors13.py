class CounterDescriptor:
    def __init__(self):
        self.count = 0

    def __set__(self, instance, value):
        self.count += 1  
        instance._value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self  
        return instance._value  
    
class MyClass:
    counter = CounterDescriptor()

obj = MyClass()
obj.counter = 10
obj.counter = 20


print(obj.counter)
print(MyClass.counter.count, "kez ayarlandı")