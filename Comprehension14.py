input = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8]

""" output = set()

for var in input:
    if var % 2 == 0:
        output.add(var)
 """

output = { var for  var in input if var % 2 == 0 }

print(output)