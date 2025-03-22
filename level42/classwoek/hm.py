list = [1,2,3,-1,-5]
list2 = []
list3 = []
for i in list:
    if i > 0:
        list2.append(i)
    elif i < 0:
        list3.append(i)
#print([sum(list2), sum(list3)])
print(list(sum(list2), sum(list3)))


