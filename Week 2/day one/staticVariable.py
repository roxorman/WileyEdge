class CsStudent:
    stream = "Stream_: cse"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        
a = CsStudent("Marco", 1)
b = CsStudent("Polo", 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

print(CsStudent.stream)
a.stream = "A_Stream: CSE"
print(a.stream)
print(b.stream)

CsStudent.stream = "mech"
print(a.stream)
print(b.stream)


