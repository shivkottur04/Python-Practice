stack=[]
n=int(input("enter number of elements:"))
for i in range(n):
    num=input("enter element:")
    stack.append(num)
print("Stack:", stack)

print("1.add\n2.sub\n3.mul\n4.div\n5.mod\n6.pow")
ch=input("enter your choice:")
result=0
if ch=='1': 
    num=int(stack.pop())
    result=num+result
elif ch=='2':   
    num=int(stack.pop())    
    result=num-result
elif ch=='3':
    num=int(stack.pop())
    result=num*result
elif ch=='4':
    num=int(stack.pop())
    result=num/result
elif ch=='5':
    num=int(stack.pop())
    result=num%result
elif ch=='6':
    num=int(stack.pop())
    result=num**result  
else:
    print("invalid input")      

print("result=",result)



