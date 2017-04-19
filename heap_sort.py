''' 1. Create an unsorted list
    2. print the unsorted list
    2. sort the list 
    3. print the sorted list 
'''

def main():
    myList = [4, 3, 1, 0, 5, 2, 6, 3, 3, 1, 6]
    print("HeapSort")
    print(" in: " + str(myList))
    # sort list 
    myList = heapSort(myList)
    print("out: " + str(myList))

def heapSort(list): 
    ''' First, use the list to create a heap object.
        Then, turn the heap into a max heap.

        '''
    heap = buildHeap(list)
    heap = buildMaxHeap(heap)    
    print("heap.data: " + str(heap.data))
    ''' First argument of range is inclusive
        2nd argument of range is not inclusive
    '''
    for i in range(len(heap.data)-1, 0, -1):
        #print("i is " + str(i))
        #print("new heap.data: " + str(heap.data))
        heap.data[0], heap.data[i] = heap.data[i], heap.data[0]
        heap.heap_size = heap.heap_size -1 
        heap = maxHeapify(heap, 0) 

    return heap.data

def buildHeap(list):
    return Heap(list)

def buildMaxHeap(heap): 
    heap.heap_size = len(heap.data)
    
    for i in range(len(heap.data)//2, -1, -1): 
        ''' Why start at //2? Draw any heap you want on a piece of 
            paper. You will see that all sub trees with a root node
            index greater than //2 is already a max heap, because they
            are leaves on the tree, so there is no need to 
            maxHeapify them.  
        '''
        #print("i is " + str(i))
        heap = maxHeapify(heap, i)
    return heap

def maxHeapify(heap, i):
    '''maxHeapify just sorts 3-node-max subtrees. 
    '''
    l = left(i)
    r = right(i)
    list = heap.data

    if ((l < heap.heap_size) and (list[l] > list[i])):
        largest = l
    else: 
        largest = i

    if (r < heap.heap_size and list[r] > list[largest]): 
        largest = r
    if (largest != i): 
        list[i], list[largest] = list[largest], list[i]
        maxHeapify(heap, largest)
    return heap

def left(i): 
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i): 
    return i//2

class Heap: 
    def __init__(self, list): 
        self.heap_size = len(list)        
        self.data = list

main()