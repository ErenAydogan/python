class Node:
    def __init__(self, datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None


class LinkedList:
    def __init__(self):
        self.headvalue=None

    def printing(self):
        printvalue = self.headvalue
        while printvalue is not None:
            if (printvalue.datavalue == "Udemy"):
                print(printvalue.datavalue)
                printvalue = printvalue.nextvalue
            else:
                printvalue = printvalue.nextvalue

x = LinkedList()
x.headvalue = Node("Joe Doe")
data2 = Node("John Doe")
data3 = Node("Python")


x.headvalue.nextvalue = data2

data2.nextvalue = data3

x.printing()