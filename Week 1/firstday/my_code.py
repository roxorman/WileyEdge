def int_to_binary(num):
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    return binary

number = 50
binary_number = int_to_binary(number)
print(binary_number)