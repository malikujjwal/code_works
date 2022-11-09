class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def sumNumbers(root):
    result = []
    currentSum = 0
    
    def dfs(root, currentSum, result):
        if root is None:
            return
            
        currentSum = (currentSum*10)+root.val   
        dfs(root.left, currentSum, result)
        dfs(root.right, currentSum, result)
        
        if root.left is None and root.right is None:
            result.append(currentSum)
        
    dfs(root, currentSum, result)

    return sum(result)
        

def main():
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)

    print(sumNumbers(root))

main()