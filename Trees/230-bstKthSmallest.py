# without the follow-up
class Solution(object):
    def kthSmallest(self, root, k):
        res = []
        def getKSmallest(node):
            if not node:
                return
            
            getKSmallest(node.left)
            
            res.append(node.val)
            
            getKSmallest(node.right)
        
        getKSmallest(root)
        return res[k-1]

# with follow-up iteratively in-order
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

