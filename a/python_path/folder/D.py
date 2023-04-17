import os
import sys

print("Welcome to D")

new_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(new_path)
import B

#finds this because the parent directory for folder2 was added to the path on line 5
import folder2.E as E

E.HelloE()

def HelloB():
    print("Hello from D")