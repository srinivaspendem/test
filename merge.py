#21. Merge Two Sorted Lists
#Merge two sorted linked lists and return it as a new list. The new list
#should be made by splicing together the nodes of the first two lists.
arr1=[1,3,4,5,6,]
arr2=[2,4,1,8,9,2,1,8,1]
arr1.extend(arr2)
arr1.sort()
print (arr1)
