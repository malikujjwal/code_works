class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def zigzagLevelOrder(root):
    result = []
    if root is None:
        return result
    
    frontier = [root]
    levelFlag = 1
    while frontier:
        levelLen = len(frontier)
        levelFlag = 0 if levelFlag == 1 else 1
        childNodes = []
        
        for _ in range(levelLen):
            fringe = frontier.pop(0)
            if levelFlag == 1:
                childNodes.insert(0, fringe.val)
            else:
                childNodes.append(fringe.val)
            if fringe.left:
                frontier.append(fringe.left)
            if fringe.right:
                frontier.append(fringe.right)
                    
        if childNodes:
            result.append(childNodes)
    
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(zigzagLevelOrder(root))

main()