#217. Contains Duplicate
#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in 
#the array, and it should return false if every element is distinct.
def checkDuplicatesWithinK(arr, n, k): 
    myset = [] 
    for i in range(n): 
        if arr[i] in myset: 
            return True
        myset.append(arr[i]) 
        if (i >= k): 
            myset.remove(arr[i - k]) 
    return False
if __name__ == "__main__": 
      
    arr = [10, 5, 3, 4, 6] 
    n = len(arr) 
    if (checkDuplicatesWithinK(arr, n, 3)): 
        print("Yes") 
    else: 
        print("No") 