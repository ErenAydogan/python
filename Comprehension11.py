feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}

cel_dict = {k:(float(5)/9)*(v-32) for (k, v) in feh.items()}

print(cel_dict)