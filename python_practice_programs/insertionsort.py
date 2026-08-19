def insertion_sort(inputlist):
    for i in range(1,len(inputlist)):
        j=i-1
        nxt_element=inputlist[i]
        while (inputlist[j]>nxt_element) and (j>=0):
            inputlist[j+1]=inputlist[j]
            j=j-1   
        inputlist[j+1]=nxt_element
        print(inputlist)
lst=[12, 11, 13, 5, 6]
print("Original list:", lst)    

insertion_sort(lst)
print("Sorted list:", lst)
