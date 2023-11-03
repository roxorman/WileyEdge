# Code this into my calculator
import itertools
from itertools import count
from itertools import product
from itertools import permutations
import math

for number in count(start=1, step=2):
    if number > 10:
        break
    print(number)
    
count=0
for i in itertools.cycle("AB"):
    if count > 7:
        break
    else:
        print(i,end=" ")
        
        count+=1
        
l = ['Marco','Python','Class']
iterators = itertools.cycle(l)

for i in range(6):
    print(next(iterators),end=" ")
    
print("\n")
print(list(itertools.repeat(25,10)))


print(list(product([1,2], repeat=2)))

print(list(permutations([1,"Marco"],2)))

a = list(permutations('12315'))
print(len(a))

# print factorial of a

def permutations(n, r):
    if n < r:
        return 0  # If r is greater than n, there are no permutations.
    return math.factorial(n) // math.factorial(n - r)

print(permutations(5, 5))
        
        
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


li1=[1,4,5,7]
li2=[1,6,5,9]
li3=[8,10,5,4]
li4=[li1,li2,li3]

print(list(itertools.chain.from_iterable(li4)))

li = [2,4,5,7,8,10,20]
print(list(itertools.islice(li,1,6,2)))
# starting position, ending position, step size

iterator = (count(start=0, step=2))

print("Even list:", list(next(iterator) for _ in range(5)))