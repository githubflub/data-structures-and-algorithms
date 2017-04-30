def main(): 
    order = ['s', 'u', 'g', 'a', 'r', 'i', 'b', 'd', 'f', 'o', 'y']
    order = list(reversed(order))
    myList = ["sugar","is", "bad", "for", "you", "s", "ss"]    
    sort(myList, order)
    print("list: " + str(myList))    

def score(word): 
    pass

def compare(x, y, order): 
    if (len(x) <= len(y)): 
        smaller = x
    else: 
        smaller = y

    for i in range(0, len(smaller)): 
        # Check greater than
        result = order.index(x[i]) - order.index(y[i])
        if result > 0: 
            return 1
        elif result < 0: 
            return -1             

    # reaching here, starting indices are the same 
    # so 
    return len(x) - len(y) 

def sort(array, order=None):
    if order is None: 
        order = ['a', 'b', 'd', 'f', 'g', 'i', 'o', 'r', 's', 'u', 'y']

    # sort based on score
    for i in range(1, len(array)): 
        j = i - 1
        while compare(array[j+1], array[j], order) < 0 and j >= 0: 
            array[j+1], array[j] = array[j], array[j+1]
            j = j - 1


main()