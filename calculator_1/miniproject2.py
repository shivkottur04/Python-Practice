def cal(op,a,b):
    if(op=='+'):
        return (a+b)
    elif(op=='-'):
        return (a-b)
    elif(op=='*'):
        return (a*b)
    elif(op=='/'):
        return (a/b)
    elif(op=='%'):
        return (a%b) 
    elif(op=='**'):
        return (a**b)
    else:                  
        return None    
print("\n-----CALCULATOR-----\n")
while(1):
    print("operations:add(+),sub(-),mul(*),div(/),mod(%),pow(**)\n")
    a=input("enter first number:")
    if(a.isdigit()==False):
        print("invalid input!! enter a number\n")
        continue
    b=input("enter second number")
    if(b.isdigit()==False):
        print("invalid input!! enter a number\n")
        continue
    a=int(a)
    b=int(b)
    ch=input("select operation:")
    result=cal(ch,a,b)
    if(result != None):
        print(a,ch,b,"=",result)
    else:
        print("invalid operator input\n")     
      
    y=input("enter 1 if you want to continue:\n")
    if(y != '1'):
        print("exiting program")
        break