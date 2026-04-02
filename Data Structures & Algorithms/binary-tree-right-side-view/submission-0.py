# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        keep track of qlen

        if qlen, append val to res
        '''
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            items_per_level = len(q)
            for i in range(items_per_level):
                node = q.popleft()
                if i == items_per_level - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
        