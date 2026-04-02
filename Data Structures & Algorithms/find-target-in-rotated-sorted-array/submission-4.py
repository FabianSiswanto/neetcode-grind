class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        find where partition is

        cases: IN EVERY STAGE YOU HAVE A SORTED HALF
            left half sorted -> l < m
                if l < target < m -> go left
                    else go right

            right half sorted -> m < r
                if m < target < r -> go right
                    else go left

        go left if m is larger than target or smaller than left
        go right if m is smaller than target or larger than right
        '''
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m

            left_half_sorted = nums[l] <= nums[m]

            if left_half_sorted:
                target_in_left_half = nums[l] <= target < nums[m]

                if target_in_left_half: # go left
                    r = m - 1
                else: # go right
                    l = m + 1

            else:  # right half sorted
                target_in_right_half = nums[m] < target <= nums[r]

                if target_in_right_half: # go right
                    l = m + 1
                else:
                    r = m - 1

        return -1