from cmsc142 import *

def test1():
    my_tree = Tree()

    my_tree.insert(-1, "bye")
    my_tree.insert(-1, "hi")
    return my_tree.search(-1) == "hi"

def test2():
    my_tree = Tree()

    try:
        my_tree.search(-1)
    except Exception as e:
        return True

def postorder(root):
    if root is None:
        return ["Lf"]
    else:
        return postorder(root.left) + postorder(root.right) + [(root.key, root.value)]

def test3():
    my_tree = Tree()
    my_tree.insert(5, "5")
    my_tree.insert(4, "4")
    my_tree.insert(6, "6")
    my_tree.insert(3, "3")

    porder = postorder(my_tree.root)
    return porder == ["Lf", "Lf", (3, "3"), "Lf", (4, "4"), "Lf", "Lf", (6, "6"), (5, "5")]

if __name__ == "__main__":
    print(f'test one passed: {test1()}')
    print(f'test two passed: {test2()}')
    print(f'test three passed: {test3()}')
    