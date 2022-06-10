

def InsertionSort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j= i-1

        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1

    return my_list

my_list = [6,1,0,8,3,2]

print(InsertionSort(my_list))
