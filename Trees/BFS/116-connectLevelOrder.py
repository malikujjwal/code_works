class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def connect(root):
    result = []
    
    if root is None:
        return None
    
    frontier = [root]
    
    while frontier:
        levelLen = len(frontier)
        
        for i in range(levelLen):
            fringe = frontier.pop(0)
            
            if i == levelLen - 1:
                fringe.next = None
            else:
                fringe.next = frontier[0]
                
            if fringe.left:
                frontier.append(fringe.left)
            if fringe.right:
                frontier.append(fringe.right)
                
    return root

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(connect(root))

main()