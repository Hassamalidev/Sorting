def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index=i
        for j in range(i+1, len(my_list)):
            if my_list[j]<my_list[min_index]:
                min_index=j
        if i !=min_index:
            temp=my_list[min_index]
            my_list[min_index]=my_list[i]
            my_list[i]=temp
    return  my_list
print(selection_sort([8,2,3,5, 9,6,1,7]))
