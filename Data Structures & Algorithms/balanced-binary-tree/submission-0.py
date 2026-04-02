# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        balanced: |h_left - h_right| <= 1
        
        traverse down -> no left and right child -> start checking heights

        '''
        if not root:
            return True

        def get_height(node):
            if not node:
                return 0
            
            h_right = get_height(node.right)
            h_left = get_height(node.left)
            
            return 1 + max(h_right, h_left)


        h_left = get_height(root.left)
        h_right = get_height(root.right)

        if abs(h_left - h_right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)