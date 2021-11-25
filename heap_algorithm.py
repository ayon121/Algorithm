#heap algorithm implementation in python

def heapify(list,n,i):
    largest = i  #root
    l = 2* i + 1 #left
    r = 2 * i + 2 #right
    
    #if left child is greater than root
    
    if l < n and list[i] < list[l]:
        largest = l
    
    #if right child is greater than root
    if r < n and list[largest] < list[r]:
        largest = r
        
    #swap root
    if largest != i:
        list[i],list[largest] = list[largest] , list[i]
        heapify(list,n,largest)
        
#the main function to sort list        
def heapsort(list):
    n = len(list)
    
    #Build a maxheap.
    for i in range(n//2-1,-1,-1):
        heapify(list , n ,i)
    
    #One by one extract elements
    for i in range (n-1,0,-1):
        list[i],list[0] = list[0],list[i] #swap
        heapify(list,i,0)

list1 = [1,59,20,56,13,43,90,47]
heapsort(list1)
print(list1)
     
