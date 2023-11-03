class Calculator:
    def __init__(self):
        self.operations = {
            1: lambda x, y: x + y,
            2: lambda x, y: x - y,
            3: lambda x, y: x * y,
            4: lambda x, y: x / y if y != 0 else "Division by zero not allowed",
            5: lambda x, y: x & y,
            6: lambda x, y: x | y,
            7: lambda x, y: x ^ y,
            8: lambda x, y: x << y,
            9: lambda x, y: x >> y,
        }

    def calculate(self, choice, x, y):
        operation = self.operations.get(choice)
        if operation:
            return operation(x, y)
        else:
            return "Invalid choice"

def main():
    calc = Calculator()
    print("Welcome to calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Bitwise AND")
    print("6. Bitwise OR")
    print("7. Bitwise XOR")
    print("8. Left shift")
    print("9. Right shift")
    print("0. Exit")
    print("______________________________")

    while True:
        try:
            choice = int(input("Enter your operator choice: "))
            if choice >= 0 and choice <= 9:
                if choice == 0:
                    exit()
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                result = calc.calculate(choice, num1, num2)
                print("______________________________")
                print("Result:", result)
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")

if __name__ == "__main__":
    main()
