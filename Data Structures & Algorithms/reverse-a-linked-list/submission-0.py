# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        new pointer assigned to head

        pointer assigned to all the nodes, store list of nodes

        pass through all, store in stack

        at top pop

        peek, put that address as the current next


        
        '''
        # redundant as prev is initialized as None
        #  if not head:
        #     return None
        
        cur = head
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node # will end up at null

        return prev
        



        

        