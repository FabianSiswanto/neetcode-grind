class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        monotonic q
        - pop items if smaller
        - add item

        if old index in q smaller than l index -> remove

        only add to res and move l once we already at size k
        '''
        indices_q = collections.deque()
        res = []

        l = 0

        for r in range(len(nums)):
            # monotonic decreasing q
            while indices_q and nums[indices_q[-1]] < nums[r]:
                indices_q.pop()

            indices_q.append(r)

            # remove outdated index
            if indices_q[0] < l:
               indices_q.popleft()

            valid_window = r >= k - 1
            if valid_window:
                max_idx = indices_q[0]
                max_item = nums[max_idx]

                res.append(max_item)
                l += 1


        return res

    