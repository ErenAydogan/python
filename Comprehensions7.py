import os

folder_path = os.path.dirname(__file__)
file_path = os.path.join(folder_path, 'python.txt')

op = open(file_path, 'r')

output = [i for i in op if "our" in i]

print(output)