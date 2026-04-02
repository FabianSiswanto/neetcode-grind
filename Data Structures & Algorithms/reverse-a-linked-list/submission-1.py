# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use temp var to keep next node to traverse

        have 2 normal var, prev and cur

        steps: fill temp, do actual logic, update normal var
        '''
        # redundant as prev is initialized as None
        #  if not head:
        #     return None
        
        prev = None
        cur = head

        while cur:
            next_node = cur.next #store temp var

            cur.next = prev #actual logic

            # update variables
            prev = cur
            cur = next_node # will end up at null

        return prev
        



        

        