import unittest
from cmsc142 import *
from hypothesis import given, example, settings
from hypothesis import strategies as st

def inorder(root):
    if root is None:
        return []
    else:
        return inorder(root.left) + [root.key] + inorder(root.right)

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
    
class Tests(unittest.TestCase):
    @given(st.lists(st.integers(), unique=True))
    @example([])
    @settings(max_examples=100)
    def test_bst_order(self, lst):
        my_tree = Tree()
        for e in lst:
            my_tree.insert(e, 0)
        self.assertEqual(sorted(lst), inorder(my_tree.root))

    @given(st.lists(st.integers()), st.integers())
    @settings(max_examples=100)
    def test_pushpop(self, lst, e):
        stack = StatelessStack(lst)
        _, new_stack = stack.push(e)
        val, _ = new_stack.pop()
        self.assertEqual(val, e)
    
    @given(st.lists(st.integers()))
    def test_is_sorted(self, lst):
        sorted_lst = merge_sort(lst)
        self.assertTrue(is_sorted(sorted_lst))

    @given(st.lists(st.integers()))
    def test_sortlen(self, lst):
        self.assertEqual(len(lst), len(merge_sort(lst)))

    @given(st.lists(st.integers()))
    def test_in_sorted(self, lst):
        sorted_lst = merge_sort(lst)
    
        for e in lst:
            self.assertTrue(e in sorted_lst)
    
if __name__ == "__main__":
    unittest.main()
