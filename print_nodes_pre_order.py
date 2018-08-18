class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = Node()

    def insert_node(self, root, data):
        if not root:
            return Node(data)
        else:
            if data >= root.data:
                current_node = self.insert_node(root.right, data)
                root.right = current_node
            else:
                current_node = self.insert_node(root.left, data)
                root.left = current_node
        return root 

    def pre_order(self, root):
        if not root:
            return 
        else:
            return self.pre_order(root.left), root.data, self.pre_order(root.right)



aTree = BinaryTree()
root = None

root = aTree.insert_node(root, 5)
root = aTree.insert_node(root, 1)
root = aTree.insert_node(root, 7)
root = aTree.insert_node(root, 2)
root = aTree.insert_node(root, 10)

print(aTree.pre_order(root))