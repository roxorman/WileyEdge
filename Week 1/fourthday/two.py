import operator
import time
L1 = [1,2,3]
L2 = [2,3,4]

t1=time.time()

a,b,c = map(operator.mul, L1, L2)
t2 = time.time()
print("The results are:", a,b,c)
print("The time taken is:", t2-t1)

t1=time.time()

for i in range(3):
    print(L1[i]*L2[i])
    
t2 = time.time()
print("The time taken is:", t2-t1)
