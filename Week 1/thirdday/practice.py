import re

def search_text(text, word):
    # Use regular expressions to search for the word in the text
    pattern = re.compile(r'\b{}\b'.format(re.escape(word)), re.IGNORECASE)
    match = re.search(pattern, text)

    if match:
        return "Found: " + match.group()
    else:
        return "Not Found"

def main():
    print("Text Processing Tool")
    text = input("Enter a sentence or text: ")
    word = input("Enter the word you want to search for: ")

    result = search_text(text, word)
    print(result)

if __name__ == "__main__":
    main()
