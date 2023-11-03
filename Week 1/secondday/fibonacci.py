# This program generates the first 20 Fibonacci numbers and 
# computes the sum of all the even Fibonacci numbers in that sequence.
# Fibonacci numbers are: 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,...

def fibonacci():
    fib_list = [1,1]
    sum_even = 0
    for i in range(2,20):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    for i in fib_list:
        if i%2 == 0:
            sum_even += i
    print("The first 20 Fibonacci numbers are: ", fib_list)
    print("The sum of all the even Fibonacci numbers in that sequence is: ", sum_even)

fibonacci()