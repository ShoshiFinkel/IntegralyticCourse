import os
import sys

#__file__ shows my current file including directory
print(__file__)

#returns the directory
print(os.path.abspath(os.path.dirname(__file__)))

# if we add another directory to the path - the import will succeed
# note visual studio code does not find the file - it is resolved at runtime
new_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'folder')
sys.path.append(new_path)
import C

C.HelloC()

def HelloB():
    print("Hello from B")
