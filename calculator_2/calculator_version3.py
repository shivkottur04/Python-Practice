from datatype import checkDataType
class calculator:
    def __init__(self):
        self.a=None
        self.b=None
        self.ch=None
        self.done=0
    def input(self):
        while(1):
            self.a=input("enter first number:")
            if checkDataType(self.a)==str or checkDataType(self.a)=="operator":
                print("invalid input!Enter again")
                #raise TypeError("invalid input for a")
            else:
                break
        while(1):        
            self.b=input("enter second number:")
            if checkDataType(self.b)==str or checkDataType(self.b)=="operator":
                print("invalid input!Enter again")
                #raise TypeError("invalid input for a")
            else:
                break    
        print("enter your choice:")    
        print("operators:")
        print("add(+)\nsub(-)\nmul(*)\ndiv(/)\nmod(%)")
        self.ch=input()
    def calculation(self):
        if checkDataType(self.a)==int:
            self.a=int(self.a)
        else:
            self.a=float(self.a)
        if checkDataType(self.b)==int:
            self.b=int(self.b)
        else:
            self.b=float(self.b)        
        self.done=0
        if self.ch=='+':
            self.result=self.a+self.b
            self.done=1 
        elif self.ch=='-':
            self.result=self.a-self.b
            self.done=1
        elif self.ch=='*':
            self.result=self.a*self.b
            self.done=1   
        elif self.ch=='/':
            try:
                self.result=self.a/self.b
                self.done=1
            except ArithmeticError:
                print("cannot divide by zero")    
        elif self.ch=='%':
            self.result=self.a%self.b 
            self.done=1
        else:
            print("invalid operator input!Try again")  
            self.done=0
    def output(self):
        if self.done==1:
            with open(r'cal.txt','a') as f:
                
                self.result=str(self.result)
                self.a=str(self.a)
                self.b=str(self.b)

                f.write("operand 1->")
                f.write(self.a)
                f.write("  operand 2->")
                f.write(self.b)
                f.write("  operation->")
                f.write(self.ch)
                f.write('\n')

                f.write("result:")
                f.write(self.a)
                f.write(self.ch)
                f.write(self.b)
                f.write("=")
                f.write(self.result)
                f.write('\n')
            print("result=",self.result)
        else:
            pass

def calculator_func():        
    while(1):        
        c=calculator()
        c.input()
        c.calculation()
        c.output()
        x=input("press 1 to continue:")
        if(x!='1'):
            break  
calculator_func()                           