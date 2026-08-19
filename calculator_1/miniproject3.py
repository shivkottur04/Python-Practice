from miniproject3_module import *                       
while(1):
    print("welcome back!!!!!!!!")
    a=input("enter first number:")
    if(a.isdigit()==False):
        print("invalid input!! enter a number\n")
        continue
    b=input("enter second number")
    if(b.isdigit()==False):
        print("invalid input!! enter a number\n")
        continue    
    a=float(a)
    b=float(b)
    cal(a,b)

    y=input("enter 1 if you want to continue:\n")
    if(y != '1'):
        print("exiting program")
        break