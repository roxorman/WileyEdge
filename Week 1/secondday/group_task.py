import random

def factorial(x):
    if(x==1):
        return 1
    return x*factorial(x-1)

def factorial_question():
    num = random.randint(1,10)
    answer = input("What is the factorial of {}?".format(num))
    correct_answer = str(factorial(num))
    if(answer != correct_answer):
        print("Incorrect \n the real answer is: \n" + str(correct_answer))
        return False
    print("Your answer is correct.")
    return True


def fibonacci():
    import random
    fib_list = [1,1]
    rand = random.randint(2,19)
    for i in range(2,20):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    missing_num = fib_list[rand] 
    fib_list[rand] = "???"

    print("The first 20 Fibonacci numbers are: ", fib_list)
    return missing_num

def fibonacci_question():
    print("One of the numbers in the Fibonacci sequence is missing")
    missing_num = fibonacci()
    
    while True:
        try:
            ans = int(input("Identify the missing number: "))
            if ans == missing_num:
                print("Congratulations! You've identified the missing number.")
                break
            else:
                print("Sorry, that's not the missing number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

fibonacci_question()




def is_palindrome(s):
    s = s.lower().replace("", "")
    return s == s[::-1]

question = [
    {"Is 'melon' a palindrome?",
     'options': [
         "Yes",
         "No"
     ],
     'correct_answer': 0
    }
    
    user_answer = int(input("Enter the number of your answer:"))



    

def main():
    factorial_question()
    fibonacci_question()

main()