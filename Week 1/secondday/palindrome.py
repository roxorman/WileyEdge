# Write a Python function that checks if a given string is a palindrome. 
# A palindrome is a word, phrase, number, or other sequences of characters 
# that reads the same forward and backward (ignoring spaces, punctuation, and capitalization)

def is_palindrome(s):
    # ignore spaces, punctuation and capitalization
    s = s.lower()
    s = s.replace(" ","")
    s = s.replace(".","")
    s = s.replace(",","")
    s = s.replace("!","")
    s = s.replace("?","")
    if s == s[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("racecar"))
print(is_palindrome("racecars"))
print(is_palindrome("race . car!"))
