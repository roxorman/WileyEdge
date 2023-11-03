class MyClass:
    def __init__(self,name = None) -> None:
        if name is None:
            print("Empty/Default Constructor called")
        else:
            self.name = name
            print("Parameterized Constructor called", self.name)
            
    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name ", self.name)
        else:
            print("Method called without name")
            
obj1 = MyClass()
obj1.method()

obj2 = MyClass("Marco")
obj2.method()