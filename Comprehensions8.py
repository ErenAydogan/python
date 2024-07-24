def x(a):
    return a ** 2

print([x(0), x(1), x(2), x(3), x(4), x(5), x(6), x(7), x(8), x(9), x(10)]) #output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


y = [x(a) for a in range(11)]
y_even = [x(a) for a in range(11) if a%2==0 ] 
y_odd = [x(a) for a in range(11) if a%2==1 ]
print(y) #output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(y_even) #output: [0, 4, 16, 36, 64, 100]
print(y_odd) #output: [1, 9, 25, 49, 81]