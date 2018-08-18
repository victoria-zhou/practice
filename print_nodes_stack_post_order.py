class Node:
    def __init__(self, data = None, left = None, right = None):
        self. data = data
        self.right = right
        self.left = left

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


    def stack_post_order(self, root):
        if not root:
            return 
        else:
            result = []
            stack = []
            node = root 
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.right
                node = stack.pop()
                result.append(node.data)
                node = node.left
        return result

aTree = BinaryTree()
root = None
root = aTree.insert_node(root, 5)
root = aTree.insert_node(root, 1)
root = aTree.insert_node(root, 2)
root = aTree.insert_node(root, 7)
root = aTree.insert_node(root, 6)
root = aTree.insert_node(root, 8)

print(aTree.stack_post_order(root))