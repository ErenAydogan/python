import time

class Lazy:
    def __init__(self, function):
        self.function=function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name]=self.function(obj)
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        pass

class Waiting:
    @Lazy
    def wait(self):
        time.sleep(3)
        return 42
    

x = Waiting()

print(x.wait)
print(x.wait)
print(x.wait)