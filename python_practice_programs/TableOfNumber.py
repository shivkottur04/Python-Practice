#1
'''r=range(4,41,4)
for i in r:
    print(i)'''

#2
'''from datatype import checkDataType
x=input("enter a number:")
y=checkDataType(x)
if y==int:
    x=int(x)
    r=range(1,11)
    for i in r:
        print(x,"*",i,"=",x*i)
else:
    print("invalid input")        '''

#3
'''def table(num):
    r=range(1,11)
    print("table of:",num)
    for i in r:
        print(num,'*',i,"=",num*i)

i,j=[int(x) for x in input("enter start and end numbers seperated by space").split()]
r=range(i,j+1)
for k in r:
    table(k)'''

#4
'''num=int(input("enter a number:"))
x=int(input("table ends with:"))  
r=range(1,x+1)
for i in r:
    print(num,"*",i,"=",num*i)  '''

#5

def table(num,y,z):
    r=range(y,z+1)
    print("table of ",num)
    for i in r:
        print(num,'*',i,"=",num*i)

from datatype import checkDataType
i,j=[(x) for x in input("enter start and end numbers seperated by space:").split()]
y=input("Table starts with:")
z=input("Table ends with:")
if checkDataType(i)==int and checkDataType(j)==int and checkDataType(y)==int and checkDataType(z)==int :
    i=int(i)
    j=int(j)
    y=int(y)
    z=int(z)
    r=range(i,j+1)
    for k in r:
        table(k,y,z)
else:
    print("input is invalid")                           