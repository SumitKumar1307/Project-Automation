import os
from os import path

print("WELCOME TO THIS SCRIPT'S CONFIGURATION FILE!")
token = input("Enter your Github Access Token: ")
print("Creating Enviorment Variable...")
if path.exists(".env"):
    f = open(".env", "w")
    f.write(f"TOKEN={token}\n")
    f.close()
else:
    f = open(".env", "w")
    f.write(f"TOKEN={token}\n")
    f.close()

print("Enviorment Variables Created.")
print("Installing Dependencies...")
os.system("pip3 install -r requirements.txt")
print("Dependencies Installed.")
print("Creating Executables...")
os.system("chmod +x new_project")
print("Executables Created!")
print("\n" + ("*" * 20) + "\n")
print("SCRIPT IS READY FOR USE, TYPE new_project --help for more information.")
