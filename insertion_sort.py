''' 1. Create an unsorted list
    2. print the unsorted list
    2. sort the list 
    3. print the sorted list 
'''

def main():
    myList = [1, 2, 1, 0]
    print("my list: " + str(myList))
    # sort list 
    myList = insertionSort(myList)
    print("my list sorted: " + str(myList))

def insertionSort(list):
    for i in range (1, len(list)): 
        element = list[i]
        ''' In a case like this, where you are binding a name (list[i])
            to a name (element), "element" doesn't actually point to 
            the name "list[i]". Rather, it points to the value that 
            "list[i]" points to. This means you can change the value
            that "list[i]" points to without changing the value that
            "element" points to. 
        '''
        j = i - 1
        while ((list[j+1] < list[j]) and (j >= 0)):            
            list[j+1], list[j] = list[j], list[j+1]
            #print("list[j] before: " + str(list[j]))            
            j = j - 1   
            #print("j is " + str(j))   
            #print("list[j] after: " + str(list[j]))      
    return list 

main()