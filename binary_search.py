def main(): 
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = int(input('Enter a number: '))
    result = find(myList, a)
    if result == None:
        print( str(a) + " is not in the list")
    else: 
        print( str(a) + " is in slot " + str(result))


def find(list, obj):    
    return _iterativeBinarySearch(list, 0, len(list)-1, obj)        


def _recursiveBinarySearch(list, p, r, obj): 
    if r < p:
        return None

    mid = (p+r)//2 
    if obj > list[mid]: 
        return _binarySearch(list, mid+1, r, obj)
    elif obj < list[mid]: 
        return _binarySearch(list, p, mid-1, obj)
    elif obj == list[mid]: 
        return mid

def _iterativeBinarySearch(list, p, r, obj):
    while r >= p: 
        mid = (p+r)//2
        if obj > list[mid]:
            p = mid+1
        elif obj < list[mid]: 
            r = mid-1
        elif obj == list[mid]:
            return mid

main()