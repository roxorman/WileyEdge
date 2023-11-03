file = open(r"C:\Users\marno\Wiley Edge\Code\Week 2\day2\marco.txt","r")
print(file.read())

with open(r"C:\Users\marno\Wiley Edge\Code\Week 2\day2\marco.txt") as file:
    data = file.read()
    for line in data:
        word = line.split()
        print(word)
        
file = open(r"C:\Users\marno\Wiley Edge\Code\Week 2\day2\marco.txt","w")
file.write("Hello World")
file.write("This is our new text file")
file.close()
