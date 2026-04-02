# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        - bfs -> have q
        - have lvl list
        - next lvl node -> start with root -> update when going over prev and put node to q
            -> append lvl list to res

        '''
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            num_nodes_per_level = len(q)
            level = []
            for _ in range(num_nodes_per_level):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level: # at last level will be empty
                res.append(level)

        return res


