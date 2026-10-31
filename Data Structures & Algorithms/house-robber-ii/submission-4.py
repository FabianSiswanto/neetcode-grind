class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        circle, take max of:
        - skip first house
        - skip last house

        max between two choices:
        - rob cur house -> cur house value + two before value
        - skip cur house -> take the prev value
        '''
        if len(nums) == 1: # handle seperately as slice skips the only house
            return nums[0]

        def helper(sub_nums):
            prev = second_prev = 0

            for n in sub_nums:
                skip_cur = prev
                rob_cur = n + second_prev
                cur_max = max(skip_cur, rob_cur)

                # update
                prev, second_prev = cur_max, prev

            return prev

        skip_first_house = helper(nums[1:])
        skip_last_house = helper(nums[:-1])

        return max(skip_first_house, skip_last_house)