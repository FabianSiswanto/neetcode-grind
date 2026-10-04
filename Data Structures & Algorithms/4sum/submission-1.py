class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        [3,2,3,-3,1,0]
        [-3,0,1,2,3]

        anchor
        find anchor 2
        two pointers 2

        base case -> do two pointers -> if k == 2
        recursive case -> try on all items -> every layer is a for loop
        - add to cur state
        - call recursively -> update target
        - remove from cur state (so other can try)
        '''
        nums.sort()
        res = []
        cur = []

        def k_sum(k, start_idx, target):
            if k == 2:
                # 2 sum two logic
                l = start_idx
                r = len(nums) - 1

                while l < r:
                    cur_sum = nums[l] + nums[r] # remember target is updated

                    if cur_sum < target:
                        l += 1
                    elif cur_sum > target:
                        r -= 1
                    elif cur_sum == target:
                        res.append(cur + [nums[l], nums[r]])

                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            # recursive case
            # every layer is an O(n) loop
            for i in range(start_idx, len(nums) - k + 1): # todo: why len - k + 1
                # check for dupes
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue

                cur.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
                cur.pop()

        k_sum(4, 0, target)
        
        return res
