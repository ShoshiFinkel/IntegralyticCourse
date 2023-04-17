
import os
import sys

print("Welcome to E")

new_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.join(new_path, 'folder'))

#this will fail because C needs to find folder2
#uncomment next line to add parent path to - then C will find folder2
#sys.path.append(os.path.join(new_path))

import C

def HelloE():
    print("Hello from E")

