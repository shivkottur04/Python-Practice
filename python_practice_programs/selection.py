def selection_sort(list):
    for idx in range(len(list)):
        min_index = idx
        for j in range(idx + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[idx], list[min_index] = list[min_index], list[idx]
        print(list)

lst=[44,64, 25, 12, 22, 11]
print("Original list:", lst)
        
selection_sort(lst)
print(lst)