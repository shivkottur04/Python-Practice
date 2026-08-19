from miniproject4_module import *
import datetime

print("\n-----CALCULATOR-----\n") 

#opening file
f=open(r'cal_txt.txt','a')
f.write("\n")

#logic to write start date and time to file
x=datetime.datetime.now()
y=x.strftime("%c")
f.write("\t\t\t\tSTART DATE AND TIME:")
f.write(y)
f.write("\n")

while(1):
    #display and input options
    print("\noperations:add(+),sub(-),mul(*),div(/),mod(%),pow(**)\n")
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))

    #input operator
    ch=input("select operation:")

    #call function cal(calculator)
    result=cal(ch,a,b)

    #converting a,b,result to string
    result=str(result)
    a=str(a)
    b=str(b)
    
    #printing result and writing it into file
    if(result != None):
        res=oper(ch)   #function to get operation name
        if(res != "invalid operator"):
            f.write(res)
            f.write(a)
            f.write(" and ")
            f.write(b)
            f.write(" is ")
            f.write(result)
            f.write("\n")    
        print("result=",result)
    else:
        f.write("invalid operator")
        print("invalid operator input\n")     


    #code to get out of the loop or continue  
    y=input("enter 1 if you want to continue:\n")
    if(y != '1'):
        print("exiting program")
       
        break

#logic to write end date and time to file
x=datetime.datetime.now()
y=x.strftime("%c")
f.write("\t\t\t\t END DATE AND TIME:")
f.write(y)
f.write("\n")
f.close()  