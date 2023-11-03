class School:
    def func1(self):
        print("This is a function inside the School class.")
        
class School1(School):
    def func2(self):
        print("This is a function inside the School1 class.")
        
class Student2(School):
    def func3(self):
        print("This is a function inside the Student2 class.")
        
class Student3(School1,Student2):
    def func4(self):
        print("This is a function inside the Student3 class.")
        
obj = Student3()
obj.func1() # This will print "This is a function inside the School class."
obj.func2() # This will print "This is a function inside the School1 class."
obj.func3() # This will print "This is a function inside the Student2 class."
obj.func4() # This will print "This is a function inside the Student3 class."



