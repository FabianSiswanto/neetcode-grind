class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        sorted ascendingly
        1-indexed answers

        solution:
        - l
        - r

        - total sum less than target -> shift l
            - else -> shift r
        '''
        l = 0
        r = len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum == target:
                return [l + 1, r + 1]

            if cur_sum < target: # need to increase target
                l += 1
            else: # need to decrease target
                r -= 1


            