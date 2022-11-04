class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def levelOrder(root):
    # BFS but pop all the elements on a level then proceed
    if root is None:
        return []
    frontier = [root]
    levelOrder = [[root.val]]
    while frontier:
        levelLen = len(frontier)
        childNodes = []
        
        for i in range(levelLen):
            fringe = frontier.pop(0)

            if fringe.left is not None:
                frontier.append(fringe.left)
                childNodes.append(fringe.left.val)
            if fringe.right is not None:
                frontier.append(fringe.right)
                childNodes.append(fringe.right.val)
            
        if childNodes:
            levelOrder.append(childNodes)
        
    
    return levelOrder

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(levelOrder(root))

main()