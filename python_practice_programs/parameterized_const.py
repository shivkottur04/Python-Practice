class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("name:",self.name)
        print("age:",self.age)
s1=student("shiv",19)
s1.disp() 