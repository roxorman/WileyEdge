class Base:
    def __init__(self):
        self.a = "MarcoPythonClass"
        self.__c = "MarcoPythonClass"
        
class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Calling protected member of base class: ")
        print(self.__c)
        
obj1 = Base()
print(obj1.a)

obj2 = Derived()
