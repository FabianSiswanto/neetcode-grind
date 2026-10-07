class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal is end, shift if we can reach it
        n = len(nums)
        target_i = n - 1

        for i in range(n - 1, -1, -1):
            can_reach_i = i + nums[i] # cur idx + jump from this idx
            can_reach_target_i = can_reach_i >= target_i

            # move goal post if can reach it
            if can_reach_target_i:
                target_i = i
        
        return True if target_i == 0 else False