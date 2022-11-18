#preoder gives the root. Inrder tell how many elements are in left of that root and the remaining in right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        Node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        Node.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        Node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return Node