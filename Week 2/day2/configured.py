from decouple import config
import os

c = os.getcwd()
print(c)
os.chdir(r"C:\Users\marno\Wiley Edge\Code\Week 2\day2")
c = os.getcwd()
print(c)
directory = "c:/Users/marno/Wiley Edg/Code/Week 2"
folder = r"C:\Users\marno\Wiley Edge\Code\Week 2\day2\dummy"

if not os.path.exists(folder):
    os.mkdir(folder)


import subprocess   
with open(r"output.txt","wb") as file:
    subprocess.check_call(["python","filemode.py"],stdin=file, text=True)





