from validation import checkDataType,checkValid_exp

#creating class
class Calculator:
    #non parameterized constructor
    def __init__(self):
        self.exp=None
        self.result=None
    #method to take input  
    def input(self):
        while(1):
            self.exp=input("enter an expression:")
            self.flag=0
            for i in self.exp:
                if checkDataType(i)==int or checkDataType(i)=="operator" or checkDataType(i)==float:
                    pass
                else:
                    self.flag=1
            if checkValid_exp(self.exp):
                pass
            else:
                self.flag=1

            if self.flag==1:
                print("invalid input!Enter again") 
            else:
                break
    #method for calculating result
    def calculation(self):
        self.done=0
        #try and except block to handle division by zero exception
        try:
            self.result=eval(self.exp)
            self.done=1
        except ArithmeticError:
            print("division by zero not possible")
    #method to display output    
    def output(self,slno):
        if self.done==1:
            print("result=",self.result)
            #opening file to write output to it
            with open(r'calc.txt','a') as f:
                f.write("\n")
                slno=str(slno)
                f.write("|")
                f.write(slno)
                f.write(".")
                f.write("   |")
                self.result=str(self.result)
                f.write("  ")
                f.write(self.exp)
                f.write("          |")
                f.write(self.result)
                f.write("            |")

#function     
def calculator_func():
    slno=0     
    while(1):
        slno=int(slno)
        slno=slno+1
        c=Calculator()
        c.input()
        c.calculation()
        c.output(slno)
        x=input("press 1 to continue:")
        if(x!='1'):
            break                