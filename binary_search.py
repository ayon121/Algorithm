#binary search algorithm using python
def binary_search(list, num):
    begin_index = 0
    end_index = len(list) - 1

    while begin_index <= end_index:
        mid_index  = begin_index + (end_index - begin_index) // 2
        midpoint_value = list[mid_index]
        if midpoint_value ==  num:
            return mid_index

        elif  num< midpoint_value:
            end_index =mid_index - 1

        else:
            begin_index =mid_index + 1

    return None


list2= [2,3,5,7,9,10,14,17,18,19,20]
n = 5
print(binary_search(list2, n))

n = 6
print(binary_search(list2, n))


       
