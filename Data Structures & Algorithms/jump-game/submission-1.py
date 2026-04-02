class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        if after jump hit 0 -> false

        edge case: last idx -> can be 0
        '''
        can_reach = 0

        for i in range(len(nums)):
            if i > can_reach:
                return False

            jump = nums[i]
            can_reach = max(can_reach, jump + i)

            target = len(nums) - 1
            if can_reach >= target:
                return True

        return False
        
        