input = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7]

output = (var for var in input if var % 2 == 0)

print("Output values using Gen Comprehension: ", end="")
for var in output:
    print(var, end='-')
