class Dog:
    attr1 = "mammal"
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Woof!", "My name is {}".format(self.name))
        
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

print("Name is {}".format(Rodger.name))
print("Name is {}".format(Tommy.name))

Rodger.speak()
Tommy.speak()