with open("test.txt","rb+") as file:
    content =file.read()
    print(content)

    file.seek(0)

    file.write(b"Hello World")

    # Point to where you want to start writing
    #file.seek(0)
    #updated_content = file.read(0)
    #print(updated_content)