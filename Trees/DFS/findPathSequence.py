class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def findPath(root, sequence):

    def dfs(root, sequence, path):
        if root is None:
            return

        if path >= len(sequence) or root.val != sequence[path]:
            return False
        if path == len(sequence)-1:
            return True

        return dfs(root.left, sequence, path+1) or dfs(root.right, sequence, path+1)

    return dfs(root, sequence, 0)
    
def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(findPath(root, [1,1,6]))

main()