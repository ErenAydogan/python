class ReadOnly:
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        return self._value
    
class MyClass:
    readonly = ReadOnly(100)

obj = MyClass()
print(obj.readonly)