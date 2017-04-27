def main():     
    bt = BinaryTree()
    a = 2
    b = 3
    c = 1
    bt.insert(a)
    bt.insert(b)
    bt.insert(c)
    bt.printTree()

class BinaryNode: 
    def __init__(self, element): 
        self.element = element
        self.key = self.element
        self.left = None
        self.right = None
        self.p = None

class BinaryTree:
    def __init__(self): 
        self.root = None

    def insert(self, element): 
        node = BinaryNode(element)
        self._insert(self.root, node)        

    # Underscore in front conventionally done to mark as private
    def _insert(self, root, node):  
        if root == None:             
            self.root = node  
        else: 
            if node.key >= root.key: 
                if root.right == None: 
                    root.right = node
                else: 
                    self._insert(root.right, node)
            else: # node.key < root.key 
                if root.left == None: 
                    root.left = node
                else: 
                    self._insert(root.left, node)

    def in_order_traversal(self, node, func):
        if node != None:
            self.in_order_traversal(node.left, func)
            func(node)
            self.in_order_traversal(node.right, func)

    def pre_order_traversal(self, node, func): 
        if node != None: 
            func(node)
            self.pre_order_traversal(node.left, func)
            self.pre_order_traversal(node.right, func)

    def post_order_traversal(self, node, func): 
        if node != None: 
            self.post_order_traversal(node.left, func)
            self.post_order_traversal(node.right, func)
            func(node)

    def printTree(self):
        print("===Your Tree===")
        print("   in order: ", end='')
        self.in_order_traversal(self.root, self._printNode)
        print()
        print("  pre order: ", end='')
        self.pre_order_traversal(self.root, self._printNode)
        print()
        print(" post order: ", end='')
        self.post_order_traversal(self.root, self._printNode)
        print()

    def _printNode(self, node):         
        print(str(node.element) + " ", end='')

main()