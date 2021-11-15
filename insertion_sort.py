#insertion sort using python.
def insertion_sort(my_list):
    for index in range (1,len(my_list)):
        current_element = my_list[index]
        position = index
        #this is for comparing current element to previous element of the list
        while current_element < my_list[position-1] and position > 0:
            my_list[position] = my_list[position-1]
            position =position-1
        my_list[position] = current_element
        
list1 = [1,3,2,4,7,9,6]
insertion_sort(list1)
print(list1)
      
