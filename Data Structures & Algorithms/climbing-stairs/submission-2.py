class Solution:
    def climbStairs(self, n: int) -> int:
        by_one_steps = 1 # leading
        by_two_steps = 1

        for i in range(n - 1):
            by_one_steps, by_two_steps = by_one_steps + by_two_steps, by_one_steps

        return by_one_steps