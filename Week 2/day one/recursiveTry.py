class recursiveFunction:
    def __init__(self,n):
        self.n = n
        print(n, "is the number")
        
    def run(self,n=None):
        if n is None:
            n = self.n
        if n<=0:
            return
        print("Running recursive function", n)
        self.run(n-1)
        
    def __del__(self):
        print("Destructor called, recursiveFunction deleted")
        
obj = recursiveFunction(5)
obj.run()

del obj

print(obj.n)