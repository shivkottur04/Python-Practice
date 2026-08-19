'''a="cat dog cat dog rabbit"
b=a.split()
c={}        #dictionary
for word in b:
    c[word]=c.get(word,0)+1   #give number of each words in a sentance
print(c)        '''

a="shiv shiv guna mega manoj chinni chinni nani"
b=a.split()
c={}
for ch in b:
    if ch in c:
        c[ch]+=1
    else:
        c[ch]=1
print(c)            