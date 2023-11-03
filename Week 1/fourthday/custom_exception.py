class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
    
try:
    raise MyError(3*2)
except MyError as error:
    print("Custom exeption raised ", error.value)
    
    
class TransitionError(MyError):
    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
        
try:
    raise TransitionError(2, 3*2, "Not allowed")
except TransitionError as error:
    print("Custom exeption raised ", error.msg)
    
a = [1,2,3]
try:
    print("second element = %d" %(a[1]))
    
    print("fourth element = %d" %(a[3]))
except:
    print("An error occurred")
finally:
    print("Finally block is executed")
    
print("______________________________________________________")

from collections import Counter

print(Counter(['B','B','A','B','C','A','B','B','A','C']))

print(Counter({'A':3, 'B':5, 'C':2}))

print(Counter(A=3, B=5, C=2))

print("______________________________________________________")

from collections import OrderedDict

print("This is a Dict:\n")

d = {}
d['b'] = 1
d['a'] = 2
d['d'] = 3
d['c'] = 4

d.pop('b')
d['b']=45
for key, value in d.items():
    print(key, value)
    
od = OrderedDict()

print("This is an Ordered Dict:\n")

od = OrderedDict()
od['c'] = 1
od['a'] = 2
od['d'] = 3
od['b'] = 4

od.pop('b')
od['b']=45
for key, value in od.items():
    print(key, value)


