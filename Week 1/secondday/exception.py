var1=6
var2=0

try:
    d = var1/var2
    print(d)
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    #del var1
    #del var2
    print("You are in final block")


print("The value of var1/var3")
#assert var2!=0, "We cannot divide by zero"
#print(var1/var2)


x = 0b10100
y=100
float_1 = 100.5
float_3 = 1.5e2

a = 5 + 3.14j

z1 = 0o215
print("the value of 0o215 is ",z1)


print(x,y)
print(float_1,float_3)
print(a,a.imag,a.real)

print("Fourth flow")
a = 5
b = 6
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a<<4)
print(a>>b)

print("Fifth flow")
a=5
print(a>3 and a<5)
print(a>3 & a<5)

print("Sixth flow") 
x=["Rose","Lotus"]
print("Rose" in x)
print("Riya" not in x)

print("seventh flow")
a = ["Rose","Lotus"]
b = ["Rose","Lotus"]
c = a
print(a is c)
print(a is not c)
print(a is b)
print(a is not b)
print(a == b)
print(a != b)

print("Eighth flow")
# code to show docstrings in python 
def add(x,y):
    """This function adds the two numbers."""
    return x+y

print(add.__doc__) # Prints the docstring of the function add()

print("Ninth flow")
num = int(input("Enter a number: "))
if num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("Tenth flow")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else: 
    print("c is the greatest")


print("Eleventh flow")
numbers = [4,2,6,7,3,5,8,10,6,2,9,3]
square = 0

squares = []

for value in numbers:
    square = value**2
    squares.append(square)
print(squares)


    