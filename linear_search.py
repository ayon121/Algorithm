list = [10,30,34,32,90,47,23,12,43,54,78]


#Linear search using while loop
def linear_search (list,n):
    i= 0
    while  i < len(list):
        if (list[i]== n):
            print("Found here")
            print(i)
            return True
        i = i + 1
    print("Didn't found here")
    return False
linear_search(list,90)
   
'''
==============================================================
'''

#Linear search using for loop
def linear_search2 (list , n):
    for i in range(len(list)):
        if list[i]== n:
            print("found at the index" ,i+1)
            return True
    else:
        print("not found")
        
linear_search2 (list , 335)
        
