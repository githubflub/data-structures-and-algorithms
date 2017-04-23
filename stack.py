def main(): 
    print("Stack")
    a = 1
    b = 2
    c = 3 
    stack = Stack(); 

    stack.push(a)
    stack.push(b)
    print(stack.toString())
    result = stack.pop()
    print ("result is " + str(result))
    print (stack.toString())



class Stack: 
    def __init__(self):
        self.array = []
        self.top = 0

    def stackEmpty(self):
        if (self.top == 0): 
            return true
        else: 
            return false

    def push(self, item):         
        self.array.append(item)
        self.top = self.top + 1

    def pop(self): 
        if (self.top == 0): 
            raise ValueError('Underflow')
            return
        else: 
            self.top = self.top - 1
            return self.array[(self.top)]

    def toString(self): 
        return str(self.array[:(self.top)])


main()