var addCost = 3; 
var multCost = 10;
var target = 4;

function Node(value, totalCost, distFromGoal) {
    this.value = value;
    this.totalCost = totalCost; 
    this.distFromGoal = distFromGoal;
}

function NodeSet() {
    this.list = []; 
}

NodeSet.prototype.add = function(node) {

    // if node is already in the array
    var index = this.list.indexOf(node.value); 
    if (index != -1) {
        // just update totalCost if necessary
        if (node.totalCost < this.list[index].totalCost) {
            this.list[index].totalCost = node.totalCost;              
        } 
        return; 
    }

    // The node isn't in the array, so...
    // add node
    this.list[this.list.length] = node; 
    // sort nodes
    this.list.sort(this.lowestCost);
    return; 
}

NodeSet.prototype.lowestCost = function(aNode, bNode){
    if (aNode.totalCost < bNode.totalCost) return -1; 
    else if (aNode.totalCost >  bNode.totalCost) return 1; 
    else return 0; 
}

NodeSet.prototype.shift = function() {
    return this.list.shift(); 
}

function number_creation(X, A, B) {
    var visited = new Set(); 
    var unvisited = new NodeSet();      

    // add 0 node     
    // Create list of unvisiteds
    var current = new Node(0, 0, 0);  
    while (true)
    {
        // add current node to visited
        visited.add(current.value); 

        // Check if current node is goal
        if (current.value == X) return current.totalCost; 

        // create 3 new nodes
        // mult
        var nextValue = current.value * 2; 
        if (!visited.has(nextValue))
        {
            var mult = new Node(nextValue,
                                current.totalCost + B,
                                Math.abs(X - nextValue)); 
            unvisited.add(mult); 
        }

        // add
        nextValue = current.value + 1; 
        if (!visited.has(nextValue)) {
            var add = new Node(nextValue,
                               current.totalCost + A,
                               Math.abs(X - nextValue));
            unvisited.add(add); 
        }
        
        // sub
        nextValue = current.value - 1; 
        if (!visited.has(nextValue)) {
            var sub = new Node(nextValue,
                               current.totalCost + A,
                               Math.abs(X - nextValue));
            unvisited.add(sub); 
        }

        // iterate current node and remove from unvisited
        current = unvisited.shift();         
    }        
}

var result = number_creation(target, addCost, multCost); 
console.log("The lowest cost is (hoping for 12): ", result); 



