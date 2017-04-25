def main(): 
    print("A to I Algorithm")
    string = "123465"
    print("string: " + string)
    print("   int: " + str(atoi(string)))

# This method is supposed to turn "123" into 123
# support negative
def atoi(string):
    result = 0
    negative = False
    if (string[0] == '-'):
        negative = True

    for i in range(0, len(string)): 
        result = result*10 + (ord(string[i]) - ord('0'))
    return result 

main()