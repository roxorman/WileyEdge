x = 101

def mainfunction():
    global x
    print(x)
    y=5
    print(y)
    x="Welcome to class"
    del y
    #print(y)
    print(x)

mainfunction()
print(x)