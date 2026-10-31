class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_ways = 1 # stop when at first position
        two_step_ways = 1

        for _ in range(n - 1): # n - 1 steps to get one_step_ways in the first step
            # left most (one step ways) -> sum of the jump 1 step and jump 2 step
            # two step ways takes in the old one step ways
            one_step_ways, two_step_ways = one_step_ways + two_step_ways, one_step_ways

        return one_step_ways