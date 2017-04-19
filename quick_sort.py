def main(): 
    print("Quick Sort")
    myList = [6, 1, 5, 2, 3]
    print(" in: " + str(myList))

    # sort
    quickSort(myList)

    print("out: " + str(myList))

def quickSort(list): 
    quickSortP(list, 0, len(list))

'''
def quickSortTest(list, p, r): 
    q = partition(list, p, r)
    print("   q: " + str(q))
    print("list: " + str(list))
    '''

def quickSortP(list, p, r):
    if (r - p > 1):     
        q = partition(list, p, r)
        quickSortP(list, p, q)
        quickSortP(list, q+1, r)

def partition(list, p, r):
    wall = p
    pivot = r - 1
    for i in range(p, r-1): 
        if (list[i] <= list[pivot]):
            # switch
            list[i], list[wall] = list[wall], list[i] 
            wall = wall + 1 
    list[pivot], list[wall] = list[wall], list[pivot]
    return wall

main()


