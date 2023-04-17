#fails when run by itself - would have to append to sys.path - parent directory for this to work here
import folder2.F

def HelloC():
    print("Hello from C")
    
folder2.F.HelloF()