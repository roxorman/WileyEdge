# Using lambda, collections, exceptions

x = {1,3,5,7,8,11,10}
y = {2,4,6,7,8,9,10}

print("Common elements in two sets: ")
print(x.intersection(y))
print("______________________________________________________")

z = [1,2,3,4,5,6,7,8,9,10,20,30,31]
print("Even numbers in list")
print(list(filter(lambda x: x%2==0, z)))
print("______________________________________________________")

print("Dictionary with swapped keys and values")
dict1 = {'a':1,'b':2,'c':3,'d':4}
print(dict1)
dict2 = {value:key for key,value in dict1.items()}
print( dict2)


