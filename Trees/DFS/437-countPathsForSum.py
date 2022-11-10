class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def pathSum(root, targetSum):
    def dfs(root, targetSum, pathCount, path):
        if root is None:
            return pathCount
        
        path.append(root.val)
        
        pathSum = 0 
        for i in range(len(path)-1, -1, -1):
            pathSum += path[i]
            
            if pathSum == targetSum:
                pathCount+=1
        
        pathCount = dfs(root.left, targetSum, pathCount, path)
        pathCount = dfs(root.right, targetSum, pathCount, path)
        
        path.pop()
        
        return pathCount
        
    pathCount = dfs(root, targetSum, 0, [])
    
    return pathCount

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(pathSum(root, 11))

main()