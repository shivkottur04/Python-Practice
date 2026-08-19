while(1):
    num=input("enter a number:")
    if(num.isdigit()):
        n=int(num)
        if (n%2==0):
            print("even") 
        else:
            print("odd")   
    else:
        print("invalid input")    
    x=int(input("if you want to continue press 1:"))  
    if(x==1):
        continue 
    else:
        break      
    
    