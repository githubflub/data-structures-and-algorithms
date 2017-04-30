def main(): 
    print("===Top Down Splay Tree===")
    elems = [0, 1, 2, 3, 4, 5]

    splay = SplayTree()
    for i in range(0, len(elems)): 
        splay.insert(elems[i])

    print("before splay: ", end="")
    splay.printTree()
    print()
    splay.root = splay.splay(5)
    print(" after splay: ", end="")    
    splay.printTree()

class SplayNode: 
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self): 
        self.root = None        

    def insert(self, element): 
        node = SplayNode(element)
        root = self.root
        if root is None: 
            self.root = node
            return

        while root is not None: 
            if node.element >= root.element: 
                if root.right is None: 
                    root.right = node
                    return
                else: 
                    root = root.right 
            else: #node.element < root.element
                if root.left is None: 
                    root.left = node  
                    return
                else:
                    root = root.left      

    def rotateWithLeftChild(self, root):
        # "duplicate" the child
        leftChild = root.left
        # replace the child with the grandchild
        root.left = leftChild.right
        # set the parent as the child's child
        leftChild.right = root 
        return leftChild


    def rotateWithRightChild(self, root): 
        # "duplicate" the child
        rightChild = root.right
        # replace the original child with the grandchild
        root.right = rightChild.left
        # set the "duplicate" child's child to the parent. 
        rightChild.left = root
        return rightChild


    def splay(self, x): 
        root = self.root

        leftTree = None
        leftTreeMax = None
        rightTree = None
        rightTreeMin = None

        
        while True:           
            if x < root.element:  
                # Check if left child exists
                if root.left is None: 
                    break
                # Rotate right in zig-zig case
                if x < root.left.element: 
                    root = self.rotateWithLeftChild(root)
                    if root.left is None:                         
                        break

                # Build right tree
                if rightTree is None: 
                    rightTree = root
                    rightTreeMin = rightTree
                else: 
                    rightTreeMin.left = root
                    rightTreeMin = rightTreeMin.left    

                # "increment" root                
                root = root.left             

            elif x > root.element:
                # Check if right child exists
                if root.right is None: 
                    break

                # Rotate left in zig-zig case
                if x > root.right.element: 
                    root = self.rotateWithRightChild(root)
                    if root.right is None:                        
                        break

                # build left tree
                if leftTree is None: 
                    leftTree = root
                    leftTreeMax = leftTree
                else: 
                    leftTreeMax.right = root
                    leftTreeMax = leftTreeMax.right

                # "increment" root                
                root = root.right

            else: # x == root.element
                break

        # Reassemble tree
        if leftTree is not None: 
            leftTreeMax.right = root.right
            root.left = leftTree
        if rightTree is not None: 
            rightTreeMin.left = root.left
            root.right = rightTree
        return root

    def _pre_order(self, node, func): 
        if node is not None: 
            func(node)
            self._in_order(node.left, func)            
            self._in_order(node.right, func)

    def _in_order(self, node, func):
        if node is not None: 
            self._in_order(node.left, func)
            func(node)
            self._in_order(node.right, func)

    def _printNode(self, node): 
        print(str(node.element) + " ", end="")

    def printTree(self):
        self._pre_order(self.root, self._printNode)

main()