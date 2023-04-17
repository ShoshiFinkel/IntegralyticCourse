#the following fails because C is not in current directory
#import C

# now try the following it works:
import folder.C

folder.C.HelloC()

#but try running C by itself - it fails

import importlib
print(importlib.util.find_spec("folder.C"))

def HelloA():
    print("Hello from A")


