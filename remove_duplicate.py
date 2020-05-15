#26. Remove Duplicates from Sorted Array
#creat a pythin program to eliminate duplicate numbers
#and to arrange them in assinding order
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
duplicate = [2, 4, 10, 20, 5,5,5,5,5,5,5,5,2, 20, 32,42,42,31,4]
duplicate.sort() 
print(Remove(duplicate))
x= 'pen'
print(x)