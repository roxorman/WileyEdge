class Mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    
    def father(self):
        print(self.fathername)
        
class Son(Mother, Father):
    def parents(self):
        print(self.fathername)
        print(self.mothername)
        
s1 = Son()
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.parents()

# explaination: https://www.geeksforgeeks.org/multiple-inheritance-in-python/