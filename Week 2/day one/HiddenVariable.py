class Myclass:
    __hiddenVariable = 0
    
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)
        
myObject = Myclass()
myObject.add(2)
myObject.add(5)

print(myObject.__hiddenVariable) # This line will cause an error
#print(myObject._Myclass__hiddenVariable) # This line will not cause an error