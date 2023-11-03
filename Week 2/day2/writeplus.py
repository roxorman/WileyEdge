file = open("test.txt","a+")

file.write("Hello World")

file.seek(0)

data = file.read()

print(data)

file.close()