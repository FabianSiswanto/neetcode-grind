class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        decision tree has two branch: WHY IS IT THIS CASE?
        1. add current item
        (backtrack in between)
        2. move on to next item

        base cases:
        - total > target
        - item out of bounds
        '''
        
        res = []

        def dfs(i, cur, total):
            if i >= len(nums) or total > target:
                return

            if total == target:
                res.append(cur.copy()) # append copy as original is still used, WHY?
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)

        return res
        