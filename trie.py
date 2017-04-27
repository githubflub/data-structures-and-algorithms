def main(): 
    # Create TrieTree
    # Put valid strings in trie tree
    tt = TrieTree()
    a = "bat"
    tt.insert(a)
    print(" contains 'bat': ", end="")
    if (tt.contains("bat")): 
        print("True")
    else: 
        print("False")    

    
    # valid strings
    validStrings = ["hello", "happy", "heart", "apple", "after", "ace"]

    # insert strings into tree
    for i in range(0, len(validStrings)):
        tt.insert(validStrings[i])


    # Look up characters and words

    print(" contains 'ha': ", end="")
    if (tt.contains("ha")): 
        print("True")
    else: 
        print("False")

    print(" contains 'horse': ", end="")
    if (tt.contains("horse")): 
        print("True")
    else: 
        print("False")

    print(" contains 'apple': ", end="")
    if (tt.contains("apple")): 
        print("True")
    else: 
        print("False")
        


class TrieNode: 
    def __init__(self):         
        self.children = TrieHashTable()

class TrieHashTable: 
    ALPHABET_LENGTH = 26

    def __init__(self, size=26):
        self.size = size
        self.table = [None] * 26 

    def contains(self, char):
        slot = self.table[self.hash(char)] 
        if slot != None: 
            return True
        else: 
            return False

    def insert(self, char):
        self.table[self.hash(char)] = TrieNode()

    def getNode(self, char): 
        slot = self.hash(char)
        return self.table[slot]


    def hash(self, char): 
        key = ord(char) - ord('0')
        return key % TrieHashTable.ALPHABET_LENGTH


class TrieTree:
    def __init__(self): 
        self.root = TrieNode()

    def insert(self, word): 
        root = self.root
        for i in range(0, len(word)):
            if root.children.contains(word[i]) == False:
                root.children.insert(word[i])
            root = root.children.getNode(word[i]) # Gets TrieNode

    def contains(self, word): 
        root = self.root
        for i in range(0, len(word)):
            if root.children.contains(word[i]) == False: 
                return False
            root = root.children.getNode(word[i])
        return True

main()