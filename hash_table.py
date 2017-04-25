def main(): 
    print("Hash Table")
    a = 13
    b = 25
    c = 39
    ht = HashTable()
    ht.insert(a)
    print("table: " + ht.toString())
    print("contains a: " + str(ht.search(a)))
    
    ht.delete(a)
    print("table: " + ht.toString())
    


# No duplicates
class HashTable():
    def __init__(self, size=10): 
        ''' Since Python doesn't have standard arrays, one way 
            to pre-allocate space for a size X "array" is as follows

            myArray[None] * X
        '''
        self.size = size 
        self.table = [None] * self.size

    def insert(self, key):
        # O(1)
        hashValue = self.hash(key)
        myList = self.table[hashValue]
        if (myList == None):
            self.table[hashValue] = []

        if (self.search(key)):
            print("no duplicates!!")
            return             

        self.table[self.hash(key)].append(key)        

    def delete(self, key): 
        hashValue = self.hash(key)
        myList = self.table[hashValue]        
        if myList == None: 
            return

        for i in range(0, len(myList)): 
            if (myList[i] == key): 
                myList.remove(key)

    def search(self, key): 
        hashValue = self.hash(key)
        myList = self.table[hashValue]
        if myList == None: 
            return

        for i in range(0, len(myList)): 
            if (myList[i] == key):
                return True
        return False                  

    def retrieve(self, key): 
        hashValue = self.hash(key)
        myList = self.table[hashValue]
        if myList == None: 
            return            
        for i in range(0, len(myList)): 
            if (myList[i] == key):
                return myList[i]        

    # In this example, the key will be numbers only. 
    def hash(self, key): 
        result = key % self.size
        #print("hashed value: " + str(result))
        return result  

    def toString(self):
        return str(self.table)

main()