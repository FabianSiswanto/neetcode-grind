# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        have dummy, tail points to that initially

        use heap to keep track of which node to use -> heap: (val, node_idx, node) -> need node_idx for tie breaker!!!
            -> pop top -> set tail next to that -> traverse top node -> if not null -> push back in heap
        '''
        heap = []
        
        for node_i, node in enumerate(lists):
            if not node:
                continue

            item = (node.val, node_i, node)
            heapq.heappush(heap, item)

        dummy = ListNode()
        tail = dummy

        while heap:
            val, node_i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            node = node.next
            if node:
                item = (node.val, node_i, node)
                heapq.heappush(heap, item)

        return dummy.next



        