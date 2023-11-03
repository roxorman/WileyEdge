def outer_func():
    var=10
    def inner_func():
        nonlocal var
        var = 14
        print("the value of var in inner_func is ",var)
    inner_func()
    print("the value of var in outer_func is ",var)

outer_func()