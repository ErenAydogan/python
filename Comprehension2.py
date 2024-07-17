list = [1,2,3,4,5]
list1 = [2,3,4,5,6]

intersection = [x for x in list for y in list1 if x == y ]
notCommonForlist = [x for x in list if not x in list1]
notCommonForlist1 = [y for y in list1 if not y in list]
nonIntersection = notCommonForlist + notCommonForlist1

print(intersection)
print(nonIntersection)