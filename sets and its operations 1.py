list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,5,6]
print("Original list : " + str(list1))
print("Original sub list : " + str(list2))
if(all(x in list1 for x in list2)):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")

    
  
