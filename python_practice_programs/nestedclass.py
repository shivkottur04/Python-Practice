class student:
    def __init__(self):
        self.name='shiv'
    def disp(self):
        print(self.name)
    class dob:
        def __init__(self):
            self.dd=4
            self.mm=9
            self.yy=2006
        def disp(self):
            print(self.dd,self.mm,self.yy)
s=student()
s.disp()
d=s.dob()
d.disp()                      