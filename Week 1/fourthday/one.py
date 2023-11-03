# map function
# iterate over a list or tuple and apply a given function or logic on it

def addition(n):
    return n+n

numbers = (1,2,3,4)
result = map(addition, numbers)
print(list(result))

result = map(lambda x: x+x, numbers)
print(list(result))

numbers1 = [1,2,3]
numbers2 = [4,5,6]
result2 = map(lambda x,y: x+y, numbers1, numbers2)
print(list(result2))

l = ["sat", "bat", "cat", "mat"]
test = list(map(list, l))
print(test)

def process_number(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
    
numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(map(process_number, numbers))

for item in result:
    print(item)
    
# get maximum  numebr in list numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
max_num = max(numbers)