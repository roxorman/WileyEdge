a=""
print(r"C:\users\marno")

print('They said "what\'s there?"')
print('''They said "what's there?"''')

integer = 10
float = 1.290
string = "Marco"

print("Hi i am integer ...... My value is %d\n Hi i am float ...... My value is %f \n Hi i am string ...... My value is %s" %(integer,float,string))

text = "apple,banana,orange,grapes"
fruits = text.split(",")
print(fruits)
print(text.index("banana"))

import re
string = "The quick brown fox jumps over the lazy dog"
pattern = r"fox"
match = re.search(pattern,string)
if match:
    print("Found")
else:
    print("Not Found")
    
def function(n1,n2=20):
    print("number 1 is: ",n1)
    print("number 2 is: ",n2)
    
def function(*args_list):
    ans = []
    for i in args_list:
        ans.append(i)
    return ans

object = function("Python","Java","C++","C#")

def function2(**kwawrgs_list):
    ans = []
    for key,value in kwawrgs_list.items():
        ans.append([key,value])
    return ans

object2 = function2(First = "Python",Second = "Java",Third = "C++",Fourth = "C#")
print(object2)

strA ='python'
print(len(strA))
print(list(strA))

# List Comprehension
Person = ["Hiya","Piyali","Dan","Tia","Marno"]  
newlist = [x for x in Person if 'i' in x]
print(newlist)

numbers = [3,5,1,7,3,9]
num = []
for n in numbers:
    num.append(n*2)
    print(num)
    
num = [n**2 for n in numbers]
print(num)

nested_list =[[i+i for i in range(5)] for i in range(3)] 
print(nested_list)

main_list=[]
for i in range(3):
    list=[]
    for j in range(5):
        list.append(j+j)
    main_list.append(list)
print(main_list)