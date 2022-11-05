class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def averageOfLevels(root):
    result = []
    
    if root is None:
        return result
    
    frontier = [root]
    
    while frontier:
        levelLen = len(frontier)
        childNodes = []
        
        for _ in range(levelLen):
            fringe = frontier.pop(0)
            childNodes.append(fringe.val)
            
            if fringe.left:
                frontier.append(fringe.left)
            if fringe.right:
                frontier.append(fringe.right)
                
        if childNodes:
            result.append(float(sum(childNodes))/levelLen)
            
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(averageOfLevels(root))

main()