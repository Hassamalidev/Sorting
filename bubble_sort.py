# arr=[8,2,3,5, 9,6,1,7]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]>arr[j+1]:
#             temp=arr[j+1]
#             arr[j+1]=arr[j]
#             arr[j]=temp
#
# print(arr)


def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0 , -1):
        for j in range(i):
            if my_list[j]>my_list[j+1]:
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list
print(bubble_sort([8,2,3,5, 9,6,1,7]))