class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.right = self.left = None
        self.data = None

    def insert(self, root, data): # when insert into a tree, a root is needed
        if not root:
            return Node(data)
        else:
            if data <= root.data:
                current_node = self.insert(root.left,data)
                root.left = current_node 
            else:
                current_node = self.insert(root.right, data)
                root.right = current_node
        return root


    def getHeight(self, root):
        if root:
            left_depth = self.getHeight(root.left)
            right_depth = self.getHeight(root.right)
            return max(left_depth, right_depth) + 1
        else:
            return - 1


aTree = BinarySearchTree()
root = None
root = aTree.insert(root, 5)
root = aTree.insert(root, 6)
root = aTree.insert(root, 3)
root = aTree.insert(root, 9)
root = aTree.insert(root, 8)
root = aTree.insert(root, 1)

print(aTree.getHeight(root))
