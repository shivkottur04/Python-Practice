lst1=[1,2,4,3]

#slicing
print(lst1[0:4])
print(lst1[:4])
print(lst1[0:4:2])
print(lst1[0:])

#methods
lst1.sort()
print(lst1)

lst2=['shiv','kottur','apple']

lst1.extend(lst2)
print(lst1)

lst1.remove('apple')
print(lst1)

#print(lst1.__len__())
print(lst1.index(1))

lst1.insert(5,'shadow')
print(lst1)

lst1.append('pubg')
print(lst1)

lst1.pop()
print(lst1)

'''print(lst1.__getitem__(1))
print(lst1.__sizeof__())'''

lst3=lst1.copy()
print("lst3",lst3)

lst1.reverse()
print(lst1)

lst1.clear()
print(lst1)

lst1=[1,2,3,4,5]
print(5 in lst1)
print(5 not in lst1)
