class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                # go left -> update res
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
