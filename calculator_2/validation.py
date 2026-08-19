def checkDataType(x):
    lst1=['^','$','!','@','#',"-",'_','{','[','}',']','|',':',';','?','<','>','.',',','`','~']
    lst=['+','-','*','/','%','(',')','**']
    if x.isdigit():
        return int
    elif x.isalnum():
        return str
    elif x in lst:
        return "operator"
    elif x in lst1:
        return None          
    else:
        return float
def checkValid_exp(exp):
    count1=0
    count2=0
    for i in exp:
        if i=='(':
            count1+=1
        elif i==')':
            count2+=1
        else:
            pass
    if count1==count2:
        return True
    else:
        return False                
