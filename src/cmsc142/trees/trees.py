class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def search_helper(self, curr, key):
        # if we can't find it
        if curr is None:
            raise Exception("Key not found")
        # follow BST invariant
        if key < curr.key:
            return self.search_helper(curr.left, key)
        elif key > curr.key:
            return self.search_helper(curr.right, key)
        else:
            return curr.value
    
    def search(self, key):
        return self.search_helper(self.root, key)
        
    def insert(self, key, value):
        self.root = self.insert_helper(self.root, Node(key, value))

    def insert_helper(self, curr, node):
        if curr is None:
            return node
        if node.key < curr.key:
            curr.left = self.insert_helper(curr.left, node)
            return curr
        else:
            curr.right = self.insert_helper(curr.right, node)
            return curr


if __name__ == "__main__":
    my_tree = Tree()
    my_tree.insert(5, "hi")
    my_tree.insert(0, "bye")
    my_tree.insert(-1, "bye")
    print(my_tree.search(-1))
    
