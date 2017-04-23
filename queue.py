def main(): 
    print("Queue")
    a = 1
    b = 2
    c = 3 
    d = 4
    e = 5
    queue = Queue(4)
    queue.enqueue(a)
    queue.enqueue(b)
    queue.enqueue(c)
    queue.enqueue(d)
    #queue.enqueue(e)
    queue.dequeue()
    queue.enqueue(e)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(a)
    queue.enqueue(b)
    queue.enqueue(c)
    queue.enqueue(d)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(e)
    print("queue: " + queue.toString())



class Queue: 
    def __init__(self, capacity): 
        self.array = []
        self.capacity = capacity
        self.length = 0 
        self.size = 0 
        self.head = 0 
        self.tail = 0 

    def enqueue(self, item): 
        if (self.size >= self.capacity):
            raise ValueError('Overflow')
            return

        if (self.length < self.capacity):
            self.array.append(item)
            self.size = self.size + 1 
            self.length = self.length + 1
            self.tail = self.tail + 1 
            if (self.tail >= self.capacity):
                self.tail = 0 
            return

        if (self.length == self.capacity): 
            self.array[self.tail] = item
            self.size = self.size + 1 
            self.tail = self.tail + 1 
            if (self.tail >= self.capacity): 
                self.tail = 0

    def dequeue(self): 
        if (self.size <= 0):
            raise ValueError('Underflow')
            return 

        returnValue = self.array[self.head]
        self.array[self.head] = '*'
        self.size = self.size - 1 
        self.head = self.head + 1 
        if (self.head >= self.capacity):
            self.head = 0 
        return returnValue

    def queueEmpty(self): 
        if (self.size == 0): 
            return true
        else:
            return false

    def toString(self): 
        return str(self.array)
main()