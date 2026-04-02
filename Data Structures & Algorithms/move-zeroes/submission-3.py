class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        my approach:
        - l and r pointer
        - swap when l = 0 and r != 0 -> after swap -> 
        - if no conditions met -> move l and r -> lead by l

        neetcode approach:
        - partition: non zero | zero
        - have index for non zero slot
        - go through items (with r pointer) -> if non zero
            -> swap with non zero slot -> update non zero slot
        """
        if len(nums) == 1:
            return nums

        non_zero_slot_i = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_slot_i] = nums[non_zero_slot_i], nums[i]
                non_zero_slot_i += 1




        # l = 0
        # r = 1

        # while r < len(nums):
        #     if nums[l] == 0 and nums[r] != 0:
        #         # swap
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r += 1
        #     elif nums[l] == 0:
        #         r += 1
        #     else: # normal case
        #         l += 1
        #         r += 1

            
        