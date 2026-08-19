lst=[x for x in input("enter numbers seperated by commas:").split(',')]
while(1):
    print("\n1.odd or even\n2.prime or not\n3.exit\n")
    ch=input("enter your choice:")
    if ch=='1':
        for i in lst:
            if(i.isspace()):
                pass
            elif(not(i.isalpha())):
                i=float(i)
                if(i%2==0):
                    print(i," is even")
                else:
                    print(i,"is odd")
            else:
                pass
            
    elif ch=='2':
        
        for i in lst:
            flag=0
            
            
            if(not(i.isalpha())):
                if(i.isnumeric()):
                    i=int(i)
                    for x in range(2,i):
                        if(i%x==0):
                            flag=1
                            break
                    if(flag==0):
                        print(i," is prime")
                    else:
                        print(i," is not prime")
                else:
                    print(i,"is not prime(only natural numbers can be considered as prime)")            
            else:
                pass
           
    elif ch=='3':
        break        
    else:
        print("invalid choice")    
         
                
       
    
