class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def findSuccessor(root, key):
    if root is None:
        return None

    frontier = [root]

    while frontier:
        fringe = frontier.pop(0)

        if fringe.left:
            frontier.append(fringe.left)
        if fringe.right:
            frontier.append(fringe.right)

        if fringe.val == key and frontier:
            return frontier.pop(0).val

    return None

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(findSuccessor(root,12))

main()