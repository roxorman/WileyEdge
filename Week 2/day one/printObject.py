class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __repr__(self) -> str:
        """
        Return a string representation of the object that can be used to recreate it.
        """
        return "test a:%s b:%s" % (self.a, self.b)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        """
        return "from str method of test a is %s, b is %s" % (self.a, self.b)
    
t =test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()