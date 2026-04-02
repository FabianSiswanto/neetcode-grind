# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        three point swap
        recursively invert left and right child
        '''
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        '''
        go over all in stack

        if stack is leaf, skip

        three point swap of children
        
        if not root:
            return None

        nodes = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            nodes.append(node)

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        node = None

        while nodes:
            node = nodes.pop()

            has_child = node.right or node.left
            if not has_child:
                continue
            
            temp = node.left
            node.left = node.right
            node.right = temp

        return node
        '''
                


        