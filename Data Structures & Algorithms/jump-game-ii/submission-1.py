class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        do level per level

        l and r pointer to keep track of cur level

        for each level -> find boundaries of next level

        go to next level
        '''
        l = r = 0
        level = 0

        while r < len(nums) - 1: # stop when r is right most, r == len(nums) - 1
            # find boundary of next level
            next_lvl_boundary = 0

            for i in range(l, r + 1):
                after_jump = i + nums[i]
                next_lvl_boundary = max(next_lvl_boundary, after_jump)

            # go to next level
            level += 1
            l = r + 1
            r = next_lvl_boundary

        return level