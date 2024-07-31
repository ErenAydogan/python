dict = {'one':{'a':10}, 'two':{'b':20}}

for (external_key, external_value) in dict.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})

dict.update({external_key:external_value})

print(dict)