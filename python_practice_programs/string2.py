str="shivKottur"
str3=" "
#slicing
print(str[0:])
print(str[0:4])
print(str[:4])
print(str[0:4:2])
#methods
print(str.count('s')) #count no. of s
print(str.count('')) #counts total no. of character including null
print(str.find('s'))  #gives index(position) of given character
print(str.isupper())  #returns true if the string is upper case
print(str.islower())    #returns true if the string is lower case
print(str.upper())      #converts str to upper case
print(str.lower())      #converts str to lower case 
print(str.index('v'))   #returns index of give character
print(str.__len__())
print(str.capitalize())     #first letter becomes capital
print(str.center(10,'-'))
print(str.isalnum())    #returns true if given string is alphabet or character
print(str.isalpha())    #
print(str.isascii())
print(str.isdigit())
print(str.isidentifier())
print(str.isnumeric())
print(str3.isspace())
print(str.isprintable())
print(str.removeprefix('shiv'))
print(str.removesuffix('Kottur'))
print(str.title())
print(str.istitle())
print(str.swapcase())
print(str.casefold())
print(str.expandtabs())
print(str.split('o'))
print(str.rsplit('o'))
print(str.splitlines())
print(str.partition('o'))
print(str.rpartition('o'))
print(str.replace('K','k'))
print(str.strip('s'))
print(str.lstrip('sh'))
print(str.rstrip('ur'))
print(str.startswith('s'))
print(str.endswith('r'))
print(str.zfill(15))
print(str.expandtabs(4))
print(str.join(' '))
print(str.rfind('o'))
print(str.rindex('o'))
print(str.rjust(15,'-'))
print(str.ljust(15,'-'))
print(str.translate(str.maketrans('sK','Sg')))
'''print(str.format("my name is {} and i am from {}".format("shiv","kottur")))
print(str.format_map({'name':'shiv','place':'kottur'}))'''
print(str.encode())





