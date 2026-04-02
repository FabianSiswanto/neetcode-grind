class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1): #basically skip one and two
            temp = one
            one = one + two #leading who gets updated
            two = temp #update to previous lead

        return one