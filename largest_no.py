#179. Largest Number
#Given a list of non negative integers, 
#arrange them such that they form the largest number.
def comparator(a, b): 
    ab = str(a) + str(b) 
    ba = str(b) + str(a) 
    return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 
      
def myCompare(mycmp): 
    class K(object): 
        def __init__(self, obj, *args): 
            self.obj = obj 
        def __lt__(self, other): 
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other): 
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other): 
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other): 
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other): 
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other): 
            return mycmp(self.obj, other.obj) != 0
    return K 
if __name__ == "__main__": 
    a = [54, 546, 548, 60, ] 
    sorted_array = sorted(a, key=myCompare(comparator)) 
    number = "".join([str(i) for i in sorted_array]) 
    print(number) 