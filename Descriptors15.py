class MyDescriptor:
    def getName(self):
        return "This is a descriptor."
    
    descriptor = property(getName)


obj = MyDescriptor()
print(obj.descriptor)