def height(root):
    result = 0
    if root.left:
        result = 1 + height(root.left)
    if root.right:
        result = 1 + height(root.right)
    
    return result