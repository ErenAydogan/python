myDict = {'temp1': 10, 'temp2':20, 'temp3':30, 'temp4':40}

cel = list(map(lambda x: (float(5)/9)*(x-32), myDict.values()))

cel_dict = dict(zip(myDict.keys(), cel))

print(cel_dict)