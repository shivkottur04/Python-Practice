def checkDataType(x):
    lst=['+','-','*','/','%','$','!','@','#','^','(',')',"-",'_','{','[','}',']','|',':',';','?','<','>','.',',','`','~']

    if x.isdigit():
        return int
        #print("int")
    elif x.isalnum():
        return str 
        #print("string") 
    elif x in lst:
        return "operator"
        #print("operator")         
    else:
        #print("float")
        return float
'''while(1):  
    x=input("enter anything:")
    checkDataType(x)        
    y=int(input("press 1 to try again"))
    if(y != 1):
        break'''

          
        