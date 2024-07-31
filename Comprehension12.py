dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

new_dict = {k:v for (k,v) in dict.items() if v>3 }
new_dict1 = {k:('even NO' if v%2==0 else 'odd NO') for (k,v) in dict.items()}
new_dict2 = {k:v for (k,v) in dict.items() if v>3 if v%2==0}

print(dict)
print(new_dict)
print(new_dict1)
print(new_dict2)
