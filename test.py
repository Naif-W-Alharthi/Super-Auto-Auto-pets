test_list = [1, 4, 2, 9, 8]
 
# printing original list
print("The original list is : " + str(test_list))
 
# declaring elements till which elements required
N = 4
 
# Get elements till particular element in list
# using index() + list slicing
temp = test_list.index(N)
res = test_list[temp:]
# rest = res[2:]
# printing result
print("Elements till N in list are : " + str(res))