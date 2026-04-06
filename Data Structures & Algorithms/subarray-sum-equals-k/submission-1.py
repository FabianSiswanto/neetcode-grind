class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        prefix sum -> build as you go
        nums[j..i] = prefix[i] - prefix[j - 1]
        k = cur_prefix - diff
        diff = cur_prefix - k

        do two sum from here
        -> map -> prefix: count
        -> default val -> if cur_prefix == k -> diff is 0 -> 0: 1

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

            diff = prefix_sum - k
            if diff in prefix_to_count:
                res += prefix_to_count[diff]

            prefix_to_count[prefix_sum] += 1

        return res


