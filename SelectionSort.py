

def selectionSort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] <  my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

my_list = [8,1,0,4,3,9,6]
print(selectionSort(my_list))