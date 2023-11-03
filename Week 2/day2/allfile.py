import os

def create_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("Hello World")
        print("File " + filename + " created successufly")
    except IOError:
        print("Error while creating file " + filename)
        
def read_file(filename):
    try:
        with open(filename,"r") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error while reading file " + filename)
        
def appened_file(filename,text):
    try:
        with open(filename, "a") as f:
            f.write(text)
        print("text appended to file " + filename + " with content: " + text)
    except IOError:
        print("Error while appending to file " + filename)
        
def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename)
    except IOError:
        print("Error while renaming file " + filename)
        
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully") 
    except IOError:
        print("Error while deleting file " + filename)
        
if __name__ == "__main__":
    filename = "example.txt"
    new_filename = "new_example2.txt"
    create_file(filename)
    read_file(filename)
    appened_file(filename, "This is a new line")
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
    
    
    