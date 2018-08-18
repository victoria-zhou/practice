class Node:
    def __init__(self, data = None, left = None, right = None):
        self. data = data
        self.right = right
        self.left = left

class BinarTree:
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


    def stack_inorder(self, root):
        if not root:
            return 
        else:
            result = []
            stack = []
            node = root 
            while node or stack:
                while node:
                    result.append(node.data)
                    stack.append(node)
                    node = node.left 
                node = stack.pop()
                node = node.right
        return result

aTree = BinarTree()
root = None
root = aTree.insert_node(root, 5)
root = aTree.insert_node(root, 1)
root = aTree.insert_node(root, 2)
root = aTree.insert_node(root, 6)
root = aTree.insert_node(root, 8)
root = aTree.insert_node(root, 7)

print(aTree.stack_inorder(root))
