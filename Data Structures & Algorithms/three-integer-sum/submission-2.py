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

        l is anchor -> shift l till diff, max l is len - 3
        if l is positive, end


        '''
        res = []
        nums.sort() #-4, -1, -1, 0, 1, 2

        for anchor in range(len(nums) - 2):
            if nums[anchor] > 0:
                break

            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue
            
            l = anchor + 1
            r = len(nums) - 1

            while l < r:
                threesum = nums[anchor] + nums[l] + nums[r]

                if threesum > 0: # too big
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[anchor], nums[l], nums[r]])
                    l += 1
                    r -= 1 # move both pointers are both alr exhausted
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
        return res


            
        