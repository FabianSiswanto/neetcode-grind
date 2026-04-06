class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        prefix sum -> build as you go
        nums[j..i] = prefix[i] - prefix[j - 1]

        do two sum from here
        -> map -> prefix: count

        loop:
        -> update prefix sum
        -> check if diff exist -> if yes -> increment count to res
        -> increment prefix count
        '''
        prefix_sum = 0
        res = 0

        prefix_to_count = defaultdict(int)
        prefix_to_count[0] = 1 # default value

        for num in nums:
            prefix_sum += num

            diff = prefix_sum - k #TODO: understand this
            if diff in prefix_to_count:
                res += prefix_to_count[diff]

            prefix_to_count[prefix_sum] += 1

        return res


