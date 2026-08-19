'''x=int(input("enter number  5 or 10:"))
assert x==5 or x==10
print("ok")   

name=input("enter your name:")
gender=input("enter gender:")
if not(name.isalpha()) or (not(gender.isalpha())):
    raise TypeError("invalid input")
print("done") '''

try:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    div=a/b
    print("result=",div)
except ArithmeticError:
    print("b should not be zero")
else:
    print("general exception caught") 
finally:
    if(b != 0):
        print("division completed")
    else:
        print("division not completed")              