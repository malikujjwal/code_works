class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def invertTree(root):
    if root is None:
        return
    
    if root.left or root.right:
        root.left, root.right = root.right, root.left
        
    invertTree(root.left)
    invertTree(root.right)
    
    return root

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(invertTree(root))

main()