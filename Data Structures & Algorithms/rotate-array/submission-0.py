class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        new index = (i)

        i + k = i
        (i + k) % len
        2 -> 0

        k = 2
        len = 4

        -3: index 3 -> 1
        2 -> 0

        (3 + 4) % 4 = 
        """
        indexToVal = {}

        for i in range(len(nums)):
            new_pos = (i + k) % len(nums)
            indexToVal[new_pos] = nums[new_pos]

            if i in indexToVal:
                nums[new_pos] = indexToVal[i]
            else:
                nums[new_pos] = nums[i]







        
        