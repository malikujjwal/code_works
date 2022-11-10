#recursive DFS
def maxDepth(root):
        if root is None:
            return 0
        
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

#iterative dfs
def maxDepth(self, root):
        stack = [[root, 1]]
        result = 0
        while stack:
            node, level = stack.pop()
            
            if node:
                result = max(result, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
                
        return result