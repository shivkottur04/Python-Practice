#function
def cal(a,b):
    print("_______________________________________________________________")
    print("|sl.no |operation       |  operand1  |  operand2   |    Result |")
    print("|______________________________________________________________|")
    print("|1.    |addition        |    ",a,"     |    ",b,"      |   ",a+b,"     |")
    print("|2.    |subtraction     |    ",a,"     |    ",b,"      |   ",a-b,"     |")
    print("|3.    |multiplication  |    ",a,"     |    ",b,"      |   ",a*b,"    |")
    print("|4.    |division        |    ",a,"     |    ",b,"      |   ",a/b,"   |")
    print("|5.    |modulus         |    ",a,"     |    ",b,"      |   ",a%b,"     |")
    print("|6.    |power           |    ",a,"     |    ",b,"      |   ",a**b,"    |")
    #print("---------------------------------------------------------")
    print("|__________________________________________________|total=",((a+b)+(a-b)+(a*b)+(a/b)+(a%b)+(a**b)),"|")
    lst=["addition","subtraction","multiplication","division","modulus","power"]
    while(1):

        ch1=input("enter your choice to be displayed(press 7 to exit):")
        if ch1=='1':
            print("addition:",a,"+",b,"=",a+b)
        elif ch1=='2':
            print("subtraction:",a,"-",b,"=",a-b)
        elif ch1=='3':
            print("multiplication:",a,"*",b,"=",a*b)
        elif ch1=='4':
            print("division:",a,"/",b,"=",a/b)
        elif ch1=='5':
            print("modulus:",a,"%",b,"=",a%b)
        elif ch1=='6':
            print("power:",a,"**",b,"=",a**b) 
        elif ch1=='7':
            break    
        else:
            print("invalid input!try again")