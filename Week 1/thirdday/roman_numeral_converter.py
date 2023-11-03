# Function to convert a number to a roman numeral in least amount of code

def convert_to_roman(num):
    roman = ""
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
        40: "XL", 50: "L", 90: "XC", 100: "C",
        400: "CD", 500: "D", 900: "CM", 1000: "M"
    }
    while num > 0:
        for key in sorted(roman_numerals.keys(), reverse=True):
            if num >= key:
                roman += roman_numerals[key]
                num -= key
                break
    return roman

def main():
    print("Roman numeral converter")
    while True:
        try:
            num = int(input("Enter a number: "))
            if num > 0:
                roman = convert_to_roman(num)
                print("Roman numeral:", roman)
            else:
                print("Invalid number")
        except ValueError:
            print("Invalid number")
            
if __name__ == "__main__":
    main()
    