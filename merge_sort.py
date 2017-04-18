''' 1. Create an unsorted list
    2. print the unsorted list
    2. sort the list 
    3. print the sorted list 
'''
import sys

def main():
    myList = [4, 2, 3, 10, 1]
    print("my list: " + str(myList))
    # sort list 
    #myList = merge(myList)
    myList = mergeSort(myList, 0, len(myList))
    #mergeSort(myList, 0, len(myList))
    print("my list sorted: " + str(myList))

def mergeSort(list, p, r):
    # determine a midpoint 
    # Remember that / is float division, // is integer division    
    q = (p+r)//2    
    #print("q: " + str(q))
    if (r - p > 1):        
        list = mergeSort(list, p, q)
        list = mergeSort(list, q, r)
        list = merge(list, p, q, r) 
    return list       

''' p, q, r are indices in the list
'''
def merge(list, p, q, r):
    ''' Create two new arrays from the list using the
        indices. 
    '''    
    left = []
    right = []
    for i in range(p, q):
        left.append(list[i])
    for i in range(q, r): 
        right.append(list[i])

    # append infinity
    left.append(sys.maxsize)
    right.append(sys.maxsize)

    ''' Iterate by inserts, there will be r - p inserts
    '''
    leftFirst = 0
    rightFirst = 0
    for i in range(p, r):
        if (left[leftFirst] < right[rightFirst]):
            list[i] = left[leftFirst]
            leftFirst = leftFirst + 1
        else: 
            list[i] = right[rightFirst]
            rightFirst = rightFirst + 1
    return list 

main()