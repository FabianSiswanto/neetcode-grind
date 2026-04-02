# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        pointer to both

        handle null edge case

        dummy -> avoid edge cases

        check if p1 or p2 is bigger 
            -> set that one as res
            -> get next

        check which one is bigger
        '''
        dummy = ListNode()

        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next #traverse pointer 1
            else: # list2 val is smaller
                tail.next = list2
                list2 = list2.next # traverse pointer 2
            # traverse tail, after already assigned its next by above
            tail = tail.next

        # handle case where one of them still exist
        if list1:
            tail.next = list1 # put list1 as the remainder
        
        if list2:
            tail.next = list2

        return dummy.next