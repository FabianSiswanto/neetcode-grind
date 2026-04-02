# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: # has subtree but no tree -> huh?
            return False
        
        if self.isSameTree(root, subRoot):
            return True

        # try on left and right subtree
        is_left_subtree = self.isSubtree(root.left, subRoot)
        is_right_subtree = self.isSubtree(root.right, subRoot)

        return is_left_subtree or is_right_subtree


    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True

        if root1 and root2 and root1.val == root2.val:
            is_left_same = self.isSameTree(root1.left, root2.left)
            is_right_same = self.isSameTree(root1.right, root2.right)

            return is_left_same and is_right_same
        else:
            return False