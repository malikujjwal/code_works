class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def hasPathSum(root, targetSum):
    if root is None:
        return False
    
    if targetSum == root.val and root.left is None and root.right is None:
        return True
    
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(hasPathSum(root, 18))

main()