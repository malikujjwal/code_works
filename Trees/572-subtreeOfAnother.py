# travel iteratively/recursively till values of both trees are same and compare
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        def compareTrees(root, subRoot):
            if not root and not subRoot:
                return True
            
            if root and subRoot and subRoot.val == root.val:
                return compareTrees(root.left, subRoot.left) and compareTrees(root.right, subRoot.right)

            return False
            
        stack = [root]
        res = False
        while stack:
            node = stack.pop()
            
            if node.val == subRoot.val:
                res = compareTrees(node, subRoot)
                if res:
                    return res
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return False