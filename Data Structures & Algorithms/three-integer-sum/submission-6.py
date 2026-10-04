class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        remove dupes -> sort
        nums: -4, -1, -1, 0, 1, 2
               a


        -1
        --
        [-1, -1, ] -> look for 2
        [-1, 0, ] -> look for 1

        sort
        
        edge cases:
        - if anchor is positive -> no right side can be negative and turn it to 0 -> break
        - if anchor is dupe -> same as before -> skip
        * need to catch duplicates in both anchor and left

        determine which way to shift depending on the actual three sum 
        '''
        res = []

        nums.sort()

        for a in range(len(nums) - 2): # -2 as need 3 items
            if nums[a] > 0:
                break

            if a != 0 and nums[a] == nums[a - 1]:
                continue

            l = a + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[a] + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                elif three_sum == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # move l if still duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res



            
        