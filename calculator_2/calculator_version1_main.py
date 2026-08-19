from calculator_version1_module import *
import datetime

#writing start date and time to file
x=datetime.datetime.now()
y=x.strftime('%X')
with open(r'calc.txt','a') as f:
    y=str(y)
    f.write("~Start time:")
    f.write(y)
    f.write("\n")     
    f.write("______________________________________")
    f.write("\n")
    f.write("|SL.NO |   Expression    |    Result  |")

#calling function
calculator_func()

#writing end date and time to file
x=datetime.datetime.now()
y=x.strftime('%X')
with open(r'calc.txt','a') as f:
    y=str(y)
    f.write("\n")
    f.write("--------------------------------------")
    f.write("\n")
    f.write("~End time:")
    f.write(y)

    f.write("\n")