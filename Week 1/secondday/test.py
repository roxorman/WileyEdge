my_list= [10,22,31,42,31,31]
count = 0
for item in my_list:
    if item == 31:
        print("item matched")
        count = count + 1
        
print("found" , count , "items")

my_str = "Hello this is a sample string"
for char in my_str:
    if char == 's':
        break
    print(char, end=' ')


