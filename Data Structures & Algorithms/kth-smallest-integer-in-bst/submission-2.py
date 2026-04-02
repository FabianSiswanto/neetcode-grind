# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_idx = 0
        stack = []
        cur = root

        while cur or stack:
            # traverse to leftmost to get smallest -> set start only
            while cur:
                stack.append(cur)
                cur = cur.left

            # here cur is null, next steps only
            cur = stack.pop()
            smallest_idx += 1
            if smallest_idx == k:
                return cur.val
            
            cur = cur.right