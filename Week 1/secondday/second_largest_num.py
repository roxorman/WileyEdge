# Write a Python program that finds the second-largest number in a list of integers. 
# You can assume that the list contains at least two distinct integers.

def second_largest_num(list):
    list.sort()
    return list[-2]
print(second_largest_num([1,2,3,4,5,6,7,8,9,10]))