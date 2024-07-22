pow = lambda x: x ** 2
print(pow(10))

numbers = [1,2,3,4,5]
y = list(map(pow, numbers))

print(y)

people_list = ['Joe', 'John', 'Alice']
makeItList = lambda x:x

final = list(map(makeItList, people_list))
print(final)

word = 'Hello'
last = list(map(makeItList, word))
print(last)
