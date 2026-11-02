class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        if mid val < right val 
            -> in sorted section -> min in left half (inclusive of mid)
        if mid val > right val
            -> not in sorted section -> min in right half  
        '''
        l = 0
        r = len(nums) - 1

        while l < r: # do nothing when l == r alr
            m = (l + r) // 2
            in_sorted_section = nums[m] < nums[r] # all elements are unique

            if in_sorted_section:
                # look to the left, keep m
                r = m
            else:
                # look to the right, dont keep m
                l = m + 1

        return nums[l]