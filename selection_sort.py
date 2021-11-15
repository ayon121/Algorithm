list = [3,5,9,0,1,2,8]


#selection sort algorithm using python "min"  method
#this code for ascending way sorting
def selection_sort(list):
    for i in range(len(list)):
        #finding maximum number with "min" method
        min_value = min(list[i:])
        min_index= list.index(min_value)

        temp = list[i]
        list[i]= list[min_index]
        list[min_index]=temp
       
selection_sort(list)
print("Ascending way sorting")
print(list)



#selection sort algorithm using python "max"  method
#this code for descending way sorting
def selection_sort(list):
    for i in range(len(list)):
        #finding maximum number with "max" method
        min_value = max(list[i:])
        min_index= list.index(min_value)

        temp = list[i]
        list[i]= list[min_index]
        list[min_index]=temp
        
selection_sort(list)
print("Descending way sorting")
print(list)


