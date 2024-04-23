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

class MyTests(unittest.TestCase):
    @given(st.lists(st.integers()), st.integers())
    @settings(max_examples=100)
    @example([], 0)
    def test_pushpop(self, stack, x):
        stack = StatelessStack(stack)
        _, new_stack = stack.push(x)
        val, _ = new_stack.pop()
        self.assertEqual(x, val)
    
    @given(st.lists(st.integers()))
    def test_is_sorted(self, lst):
        sorted_lst = merge_sort(lst)
        self.assertTrue(is_sorted(sorted_lst))

    @given(st.lists(st.integers()))
    @settings(max_examples=100)
    def test_sortlen(self, lst):
        sorted_lst = merge_sort(lst)
        self.assertTrue(len(lst) == len(sorted_lst))

    @given(st.lists(st.integers()))
    @settings(max_examples=100)
    def test_idempotency(self, lst):
        sorted_lst = merge_sort(lst)
        sorted_sorted_lst = merge_sort(merge_sort(lst))
        self.assertEqual(sorted_lst, sorted_sorted_lst)

    @given(st.lists(st.integers()))
    def test_in_sorted(self, lst):
        sorted_lst = merge_sort(lst)

        for e in lst:
            self.assertTrue(e in sorted_lst)

    @given(st.lists(st.integers()))
    def test_inorder(self, lst):
        tree = Tree()
        for x in lst:
            tree.insert(x, 0)
        
        traversal = inorder(tree.root)
        self.assertTrue(is_sorted(traversal))


if __name__ == "__main__":
    unittest.main()