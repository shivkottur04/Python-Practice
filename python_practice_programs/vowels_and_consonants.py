str=input("input a word:")
if str.isalpha():
    print(str)
    str=str.upper()
    x=str.count('')
    print("total characters:",x-1)
    count=0
    for i in str:
        #if i =='A' or i =='E'  or i =='I'  or i =='O'  or i =='U' :   
        if i in "AEIOU":
            count=count+1
    print("vowels:",count)
    print("consonants:",x-count-1)
else:
    print("invalid input")
