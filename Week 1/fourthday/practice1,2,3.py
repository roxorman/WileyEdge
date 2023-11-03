from itertools import count
import time
import operator

# Use map to perform complex function over list
t1=time.time()
list1=[]
for num in count(start=2, step=2):
    if num > 1550:
        break
    list1.append(num)

def arithmetic(num):
    return (num*num)*5/10
    

result = list(map(arithmetic, list1))

print(result)
t2 = time.time()

print("The time taken is:", t2-t1)


class Student():
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def add_course(self, course_name, grade, credits):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits
        
    

    #def view_student_information(self):
        # Display student information
        
        


class Solution:
    def missingNumber(self, nums):
        x = max(nums)
        for i in range(0,x+1):
            if i not in nums:
                return i
            

