dict = {'a':1, 'b':2, 'c':3, 'd':4}

x = dict.items()
y = dict.keys()
z = dict.values()
print(x) #dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(y) #dict_keys(['a', 'b', 'c', 'd'])
print(z) #dict_values([1, 2, 3, 4])


new_dict = {key:value**2 for (key,value) in dict.items()}
print(new_dict) #{'a': 1, 'b': 4, 'c': 9, 'd': 16}

new_dict2 = {key*2:value for key, value in dict.items()}
print(new_dict2) # {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4}

new_dict3 = {i:i**2 for i in range(1, 20, 2)}
print(new_dict3)