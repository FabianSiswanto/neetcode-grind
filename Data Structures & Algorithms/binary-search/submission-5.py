class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif target < nums[m]:
                # go left
                r = m - 1
            else:
                # go right
                l = m + 1

        return -1