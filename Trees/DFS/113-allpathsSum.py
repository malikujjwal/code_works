class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def pathSum(root, targetSum):
    path = []
    resultPath = []
    
    def dfs(root, targetSum, path):
        if root is None:
            return
        
        path.append(root.val)
        
        if root.val == targetSum and root.right == None and root.left == None:
            resultPath.append(list(path))  
    
        dfs(root.left, targetSum - root.val, path)
        dfs(root.right, targetSum - root.val, path)
        path.pop()
        
    dfs(root, targetSum, path)
    
    return resultPath 

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(pathSum(root, 18))

main()