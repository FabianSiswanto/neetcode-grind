class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        - l and r pointer
        - swap when l = 0 and r != 0 -> after swap -> 
        - if no conditions met -> move l and r -> lead by l

        101
        110
        """
        if len(nums) == 1:
            return nums

        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                # swap
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] == 0:
                r += 1
            else: # normal case
                l += 1
                r += 1

            
        