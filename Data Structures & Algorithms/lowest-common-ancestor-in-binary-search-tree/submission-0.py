# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        cases:
            - if p & q < me -> go left
            - if me < p & q -> go right
            - if p <= me <= q or q <= me <= q -> i am LCA

        not needed as this is BST:
        - find p and q from root -> keep track of recent ancestor
        - if ancestor match -> put in res
        - ancestor match:
            - l == p and r == q/ other way around
            - cur == p and (l == q or r == q)/ other way around       
        '''
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
            
        return root
        