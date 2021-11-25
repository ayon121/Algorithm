#for jump search we need linear search
#there is two part in jump search
'''In the 1st part it will do jump search and
in the 2nd part it it will do linear search 
'''

#Linear search using while loop
def linear_search (list,n , i):
    i = 0
    while  i < len(list):
        if (list[i]== n):
            print("Found here in index:-")
            print(i)
            return True
        i = i + 1
    print("Didn't found here")
    return False



#jump search using python
import math

def jump_search(list, num):
    print("Entering Jump Search")
    n = len(list)               #length of the list 
    m = int(math.sqrt(n))       #Step length
    i= 0                        #Starting interval
    
    while i != len(list)- 1 and  list[i]< num:
        print("Processing Block -{}".format(list[i:i+m]))
        
        if list[ i + m-1] == num:   	    #found the search key
            print("Found here in index:-")
            print(i + m -1)
            return
     
        elif list [i + m -1] > num:
            B = list[i: i +m -1]
            return linear_search(B , num , i)
        
        i += m
        
    B = list[i: i + m]
    print("Processing Block -{}".format(B))
    return linear_search(B , num , i)
            

#it is the implemantation       
list1 = [12,23,34,45,56,67,89,90,95]
num = 34
jump_search(list1, num)
    
    
    
