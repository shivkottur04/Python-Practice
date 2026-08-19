x=1
while(x==1):
    a=int(input("enter number:"))
    flag=0
    for i in range(2,a):
        if(a%i==0):
            flag=1
            break
    if(flag==1):
        print("not prime")
    else:
        print("prime")        
    x=int(input("press 1 if you want to continue!!"))
        
    