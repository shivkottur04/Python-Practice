text="Hello World...!!!"
vowels=0
consonent=0
for i in text.lower():
    if i.isalpha():
        if i in "aeiou":
            vowels+=1
        else:
            consonent+=1
print("total vowels:",vowels)
print("total consonents:",consonent)                