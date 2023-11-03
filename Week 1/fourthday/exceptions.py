x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("There was a type error!")
    
def fun(a):
    if a> 4:
        b = a/(a-3)
    print("this is b", b)
    
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("There was a zero division error!")
except NameError:
    print("There was a name error!")
    

def example():
    try:
        int("N/A")
    except ValueError as e:
        raise RuntimeError("A parsing error occurred") from e
    
try:
    example()
except RuntimeError as e:
    print("It didn't work:", e) 
    if e.__cause__:
        print("Cause:", e.__cause__)