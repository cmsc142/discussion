from cmsc142 import *

def test1():
    my_tree = Tree()
    my_tree.insert(-1, "bye")
    my_tree.insert(-1, "hi")
    
    return "hi" == my_tree.search(-1)

if __name__ == "__main__":
    test1()