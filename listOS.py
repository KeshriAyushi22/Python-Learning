import os

print("Current Directory:", os.getcwd())

for item in os.listdir():
    print(item)