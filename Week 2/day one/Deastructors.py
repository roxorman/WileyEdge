class Employee:
    def __init__(self):
        print("Employee Created")
        
    def __del__(self):
        print("Destructor called, Employee deleted")
        
def create_obj():
    print("Making Object...")
    obj = Employee()
    print("Function end...")
    return obj

obj=create_obj()
print("Program end...")