def main(): 
    bob = Human()
    bob.legs = 2 
    print("bob has " + str(bob.legs) + " legs.")

class Animal:
    def __init__(self): 
        self.legs = None

class Human(Animal):
    def __init__(self): 
        super().__init__()
        self.arms = None

main()