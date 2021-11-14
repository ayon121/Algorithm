
#bubble sort algorithm using python
def bubble_sort(num):
    for i in range (len(num)-1,0,-1):
        for j in range (i):
            #here it is checking if the number is bigger than next one
            if num[j]> num[j+1]:
                #this is for swaping number
                temp = num[j]
                num[j]= num[j+1]
                num[j+1]= temp
                
        #this print function will print full bubble sorting process
        print(num)
                
list = [1,6,8,5,9,2,3]
#here calling the fucntion
bubble_sort(list)
print("This is the final list after bubble sorting process:-")
#this print function will print the final list
print(list)
