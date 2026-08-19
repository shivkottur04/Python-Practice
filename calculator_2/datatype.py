def checkDataType(x):
    lst=['+','-','*','/','%','$','!','@','#','^','(',')',"-",'_','{','[','}',']','|',':',';','?','<','>','.',',','`','~']
    
    if x.isdigit():
        return int
    elif x.isalnum():
        return str 
    elif x in lst:
        return "operator"         
    else:
        return float