class Solution(object):
    def rightSideView(self, root):
        result = []
        
        if root is None:
            return result
        queue = [root]
        while queue:
            levelLen = len(queue)
            
            for i in range(levelLen):
                node = queue.pop(0)
                if i == levelLen - 1:
                    result.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result