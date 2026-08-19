from datatype import checkDataType
class calculator:
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
            print("invalid input")  
            self.done=0
    def output(self):
        if self.done==1:
            print("result=",self.result)
        else:
            pass
c=calculator()
c.input()
c.calculation()
c.output()                     

        
        