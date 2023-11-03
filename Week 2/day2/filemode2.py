with open ("example.txt","wb") as file:
    data = b'this is a binary \n file'
    file.write(data)
    
with open("example.txt", "wb+") as file:
    data = b"this is a binary \n file"
    file.write(data)
    file.seek(0)
    print(file.read())






