s1={1,2,3,4,5}
s2={5,6,7,8,9,10}
s3={4}
print(s1.intersection(s2))    #s1 intersection
print(s1.union(s2))    #s1 union s2
s1.add(0)  #adds 0 to s1
print(s1)
s3=s1.copy()    #copies elements of s1 to s3
print("s3:",s3)
print(s1.difference(s2))  #removes common element of s1 and s2 from s1
s1.pop()    #pops first element
print(s1)
s1.remove(5)   #removes 5
print(s1)

s3.clear()  #clears s3
print(s3)

s4={1,2,3,4,5,6,7}
s4.discard(7)    #discards 7
print("s4=",s4)
s4.update(s2)    #inserts elements of s2 to s4
print("s4=",s4)



s5={1,2,3,4,5}
s6={1,2}
s7={3,4}
print(s5.issuperset(s6))  #s5 is superset of s6
print(s6.issubset(s5))   #s6 is subset of s5
print(s6.isdisjoint(s7))  #returns true if there are no elements in common