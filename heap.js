function main() {
    console.log("I am going to make a heap."); 
    let myArray = [5, 2, 7, 3, 44, 8, 3, 1]; 
    let max = new MaxHeap(myArray).getMax(); 
    console.log("Max is:", max);      
}


function MaxHeap(list) {
    this.list = list; 
    this.heap_size = list.length; 
    
    // heapifiy all the subtrees
    for (let i = Math.floor(this.heap_size/2); i >= 0; i--)
    {         
        this.maxHeapify(i);  
    }
}

MaxHeap.prototype.getIndexOfLeftChild = function(parentIndex) {
    return (2 * parentIndex + 1); 
}

MaxHeap.prototype.maxHeapify = function(parent) {
    // maxHeapify's purpose is to re-order a 
    // binary subtree such that every parent node
    // is larger than its children
    // maxHeapify looks at subtrees that 
    // contain at most 3 nodes. It sets the 
    // root of the subtree to the largest
    // value that was in the subtree. In case of a 
    // swap maxHeapify also applies itself to
    // the swapped child. 
     
    // Assume both children exist
    let leftChildExists = true; 
    let rightChildExists = true; 

    // Get indices of left and right children
    let leftChild = this.getIndexOfLeftChild(parent); 
    let rightChild = leftChild + 1;

    // Check whether children actually exist
    if (leftChild >= this.heap_size) {
        leftChildExists = false; 
    }
    if (rightChild >= this.heap_size) {
        rightChildExists = false; 
    }

    // Assume parent is the largest
    let largest = parent; 

    // Compare root to left child 
    if (leftChildExists && this.list[leftChild] > this.list[parent])
    {
        // set largest to the index of the left child
        largest = leftChild; 
    }

    // Compare largest to right child
    if (this.list[rightChild] > this.list[largest] && rightChildExists) 
    {
        // set largest to index of right child
        largest = rightChild; 
    }

    // Do a swap if largest is not parent
    if (largest != parent) 
    {
        // swap 
        let temp = this.list[parent]
        this.list[parent] = this.list[largest]; 
        this.list[largest] = temp; 

        // max heapify the child
        this.maxHeapify(largest); 
    }
}


MaxHeap.prototype.getMax = function() {        
    return this.list[0]; 
}

main(); 