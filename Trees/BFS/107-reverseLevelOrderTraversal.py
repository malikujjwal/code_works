class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def levelOrderBottom(root):
    result = []
    
    if root is None:
        return result
    
    frontier = [root]
    result.append([root.val])
    
    while frontier:
        levelLen = len(frontier)
        childNodes = []
        
        for _ in range(levelLen):
            fringe = frontier.pop(0)
            
            if fringe.left:
                frontier.append(fringe.left)
                childNodes.append(fringe.left.val)
                
            if fringe.right:
                frontier.append(fringe.right)
                childNodes.append(fringe.right.val)
            
        if childNodes:
            result.insert(0, childNodes)
        
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(levelOrderBottom(root))

main()