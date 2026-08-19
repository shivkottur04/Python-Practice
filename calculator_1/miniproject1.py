while(1):
    while(1):
        a=input("enter first number:")
        if not(a.isdigit()):
            print("invalid input!Enter again")
            continue
        else:
            break

    while(1):
        b=input("enter second number:")
        if not(a.isdigit()):
            print("invalid input!Enter again")
            continue
        else:
            break 
    print("operators:+,-,*,/,%")
    ch=input("enter your choice:") 
    a=int(a)
    b=int(b)
    if ch=='+':
        print('result=',a+b)
    elif ch=='-':
        print("result=",a-b) 
    elif ch=='*':
        print("result=",a*b)        
    elif ch=='/':
        print("result=",a/b)   
    elif ch=='%':
        print("result=",a%b) 
    else:
        print("invalid choice")

    y=input("press 1 to continue")
    if y != '1':
        break               