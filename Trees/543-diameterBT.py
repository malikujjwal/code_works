#start from last node, return height of the tree everytime and calculate the diamter from it
# this way every root gets traversed only once because we are send the height back and calculating the diamter based on it.

def diameterOfBinaryTree(self, root):
    treeDiameter = [0]
    
    def dfs(root):
        if root is None:
            return -1
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        treeDiameter[0] = max(treeDiameter[0], 2+left+right)
        
        return 1+max(left, right)
    
    dfs(root)
    return treeDiameter[0]