class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def lca(root, v1, v2):
    current_node = root
    if current_node == None:
        return None
#     small = min(v1, v2)
#     large = max(v1, v2)
#     if small <= current_node.info <= large:
#         return current_node
    
#     if large < current_node.info:
#         return lca(current_node.left, small, large)
#     else:
#         return lca(current_node.right, small, large)
    if (v1 <= current_node.info and v2 >= current_node.info) or (v1 >= current_node.info and v2 <= current_node.info):
        return current_node
    else:
        if v1 <= current_node.info:
            current_node = root.left
            return lca(current_node, v1, v2)
        else:
            current_node = root.right
            return lca(current_node, v1, v2)


tree = BinarySearchTree()

for infor in [4, 2, 3, 1, 7, 6]:
    tree.create(infor)

print(lca(tree.root, 1, 7))