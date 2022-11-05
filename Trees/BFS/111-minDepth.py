class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def minDepth(root):
    if root is None:
        return 0
    
    frontier = [root]
    depth = 0
    
    while frontier:
        depth += 1
        levelLen = len(frontier)
    
        for _ in range(levelLen):
            fringe = frontier.pop(0)
            
            if fringe.left is None and fringe.right is None:
                return depth
            if fringe.left:
                frontier.append(fringe.left)
            if fringe.right:
                frontier.append(fringe.right)
            
    
    return depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(minDepth(root))

main()