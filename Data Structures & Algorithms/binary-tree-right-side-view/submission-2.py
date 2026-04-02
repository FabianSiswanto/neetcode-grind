# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        dfs(node, depth):
        - try go right, then try to go left
        - find first right most with next_depth ->
        if next_depth == depth -> len(res) == depth -> append node val

        bfs:
        keep track of qlen

        if qlen - 1, append val to res
        '''
        if not root:
            return []

        res = []

        def dfs(node, depth):
            if not node:
                return

            next_depth = len(res)
            if depth == next_depth:
                res.append(node.val)

            # dfs right first as we looking for right most
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        # bfs
        # q = deque([root])

        # while q:
        #     items_per_level = len(q)
        #     for i in range(items_per_level):
        #         node = q.popleft()
        #         if i == items_per_level - 1: # last item in level
        #             res.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        return res
        