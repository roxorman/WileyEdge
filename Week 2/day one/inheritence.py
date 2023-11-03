class Person(object):
    def __init__(self, name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def idnumber(self):
        print(self.idnumber)
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.idnumber))
        
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber) # Or to be called before or after your choice - Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post
        
        
    def details(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {}".format(self.idnumber))
        print("My post is {}".format(self.post))
        print("My salary is {}".format(self.salary))
        
a = Employee("Rahul", 886012, 20000, "Intern")
a.display()
a.details()
        