lst=[1,4,2,5,6,3]
key=int(input("enter the element to be searched:"))
count=0
for i in range(len(lst)):
    if lst[i]==key:
        print("element found at position",i)
        count=1
        break
if count == 0:
    print("element not found")    