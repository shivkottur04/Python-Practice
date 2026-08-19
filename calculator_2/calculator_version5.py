from validation import checkDataType,checkValid_exp
import datetime

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
            with open(r'calcu.txt','a') as f:
        
                slno=str(slno)
            
                f.write(slno)
                f.write(".")
                self.result=str(self.result)
                f.write("expression->")
                f.write(self.exp)
                f.write('\n')
                f.write("Result: ")
                f.write(self.exp)
                f.write("=")
                f.write(self.result)
                f.write("\n")

#writing start date and time to file
x=datetime.datetime.now()
y=x.strftime('%c')
with open(r'calcu.txt','a') as f:
    y=str(y)
    f.write("\t\t\t\t\t\t~Start time:")
    f.write(y)
    f.write("\n")     

calculator_func()

#writing end date and time to file
x=datetime.datetime.now()
y=x.strftime('%c')
with open(r'calcu.txt','a') as f:
    y=str(y)
    f.write("\t\t\t\t\t\t~End time:")
    f.write(y)
    f.write("\n")