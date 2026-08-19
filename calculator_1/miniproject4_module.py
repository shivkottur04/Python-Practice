def cal(op,a,b):
    if(op=='+'):
        return (a+b)
    elif(op=='-'):
        return (a-b)
    elif(op=='*'):
        return (a*b)
    elif(op=='/'):
        return (a/b)
    elif(op=='%'):
        return (a%b) 
    elif(op=='**'):
        return (a**b)
    else:              
        return "invalid operator" 
def oper(ch):
    if(ch=='+'):
        return "addition of:"
    elif(ch=='-'):
        return "subtraction of:"
    elif(ch=='*'):
        return "multiplication of:"
    elif(ch=='/'):
        return "division of:"
    elif(ch=='%'):
        return "modulus of:"
    elif(ch=='**'):
        return "power of:"        
    else:
        pass

