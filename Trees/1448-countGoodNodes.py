# most asked question of microsoft in 2021 - PreOrder Traversal
# pass the max value as you dfs down the tree. The time complexity would be O(log n) (best case) and O(n) (worst case)
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maxVal):
            if node is None:
                return 0
            
            maxVal = max(node.val, maxVal)
            count = 1 if node.val >= maxVal else 0
                
            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)
            
            return count
        
        return dfs(root, root.val)