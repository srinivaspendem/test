print("      |     |     ")
print("   1  |   2 |   3 ")
print("-------------------")
print("      |     |     ")
print("   4  |   5 |   6 ")
print("-------------------")
print("      |     |     ")
print("   7  |   8 |   9 ")
print ("choose the numbers alternatly",end=' ')
InputA = set()
InputB = set()
a = input("player 1, Enter your input:")
InputA.add(a)
b = input("player 2, Enter your input:")
InputB.add(b)
a = input("player 1, Enter your input:")
InputA.add(a)
b = input("player 2, Enter your input:")
InputB.add(b)
a = input("player 1, Enter your input:")
InputA.add(a)
if(InputA==set([1,2,3])):
    print("player 1 win")
elif(InputA==set([4,5,6])):
    print("player 1 win")
elif(InputA==set([7,8,9])):
    print("player 1 win")
elif(InputA==set([1,4,7])):
    print("player 1 win")
elif(InputA==set([2,5,8])):
    print("player 1 win")
elif(InputA==set([3,6,9])):
    print("player 1 win")
elif(InputA==set([1,5,9])):
    print("player 1 win")
elif(InputA==set([3,5,7])):
    print("player 1 win")
else:
    b = input("player 2, Enter your input:")
    InputB.add(b)
    if(InputB==set(1,2,3)):
        print("player 2 win")
    elif(InputB==set(4,5,6)):
        print("player 2 win")
    elif(InputB==set(7,8,9)):
        print("player 2 win")
    elif(InputB==set(1,4,7)):
        print("player 2 win")
    elif(InputB==set(2,5,8)):
        print("player 2 win")
    elif(InputB==set(3,6,9)):
        print("player 2 win")
    elif(InputB==set(1,5,9)):
        print("player 2 win")
    elif(InputB==set(3,5,7)):
        print("player 2 win")
    else:
        a = input("player 1, Enter your input:")
        InputA.add(a)
        if(InputA==set(1,2,3)):
            print("player 1 win")
        elif(InputA==set(4,5,6)):
            print("player 1 win")
        elif(InputA==set(7,8,9)):
            print("player 1 win")
        elif(InputA==set(1,4,7)):
            print("player 1 win")
        elif(InputA==set(2,5,8)):
            print("player 1 win")
        elif(InputA==set(3,6,9)):
            print("player 1 win")
        elif(InputA==set(1,5,9)):
            print("player 1 win")
        elif(InputA==set(3,5,7)):
            print("player 1 win")
        else:
            b = input("player 2, Enter your input:")
            InputB.add(b)
            if(InputB==set(1,2,3)):
                print("player 2 win")
            elif(InputB==set(4,5,6)):
                print("player 2 win")
            elif(InputB==set(7,8,9)):
                print("player 2 win")
            elif(InputB==set(1,4,7)):
                print("player 2 win")
            elif(InputB==set(2,5,8)):
                print("player 2 win")
            elif(InputB==set(3,6,9)):
                print("player 2 win")
            elif(InputB==set(1,5,9)):
                print("player 2 win")
            elif(InputB==set(3,5,7)):
                print("player 2 win")
            else:
                a = input("player 1, Enter your input:")
                InputA.add(a)
                if(InputA==set(1,2,3)):
                    print("player 1 win")
                elif(InputA==set(4,5,6)):
                    print("player 1 win")
                elif(InputA==set(7,8,9)):
                    print("player 1 win")
                elif(InputA==set(1,4,7)):
                    print("player 1 win")
                elif(InputA==set(2,5,8)):
                    print("player 1 win")
                elif(InputA==set(3,6,9)):
                    print("player 1 win")
                elif(InputA==set(1,5,9)):
                    print("player 1 win")
                elif(InputA==set(3,5,7)):
                    print("player 1 win")
                else:
                    print("DRAW")