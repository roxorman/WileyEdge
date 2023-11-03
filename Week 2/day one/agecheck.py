from datetime import date

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def isAdult(age):
        return age > 18
    
person1 = Person('Marco', 26)
person2 = Person.fromBirthYear('Reilley', 2003)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))
print(Person.isAdult(17))

