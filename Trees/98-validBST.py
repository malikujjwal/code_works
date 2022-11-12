# don't just compare root with left and right nodes. The whole subtree should follow the rule.
# set paramters for each root node where it should be greater than left value and less than right value.
# will run in 0(n)
class Solution(object):
    def isValidBST(self, root):
        def dfs (root, left, right):
            if not root:
                return True

            if not (root.val > left and root.val < right):
                return False

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        
        return dfs(root, float("-inf"), float("inf"))