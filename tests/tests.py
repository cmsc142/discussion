from cmsc142 import *
import unittest

class MyTests(unittest.TestCase):
    def setUp(self):
        self.my_tree = Tree()

    def test0(self):
        self.my_tree = Tree()

        self.my_tree.insert(-1, "bye")
        self.assertEqual(self.my_tree.root.value, "bye")

    def test1(self):
        self.my_tree.insert(-1, "hi")
        self.assertEqual(self.my_tree.search(-1), "hi")

    def test2(self):
        my_tree = Tree()
        
        with self.assertRaises(Exception):
            my_tree.search(-1)

    def test3(self):
        def inorder(root):
            if root is None:
                return []
            else:
                return inorder(root.left) + [root.key] + inorder(root.right)

        my_tree = Tree()
        my_tree.insert(5, "5")
        my_tree.insert(4, "4")
        my_tree.insert(6, "6")
        my_tree.insert(3, "3")

        ordered = inorder(my_tree.root)
        self.assertEqual(ordered, [3,4,5,6])

if __name__ == "__main__":
    unittest.main()
    
