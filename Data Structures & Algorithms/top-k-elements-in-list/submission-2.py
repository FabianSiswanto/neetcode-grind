class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        freq map

        keep heap of size k
        heap store [frequency, number]

        use bucket -> freq: list of nums
        traverse from back -> add nums -> till len(res) == k
        '''
        counter = Counter(nums)

        #bucket -> freq: list of nums -> use list of 0...len(nu s)
        bucket_size = len(nums) + 1 # as 0...len(nums) inclusive
        bucket = [ [] for i in range(bucket_size) ]
        
        for num, freq in counter.items():
            bucket[freq].append(num)

        res = []
    
        # skip bucket[0] -> not used
        for i in range(len(bucket) - 1, 0, -1):
            nums = bucket[i]

            for num in nums:
                res.append(num)

                if len(res) == k:
                    return res


        ''' heap solution
        heap = []

        # build freq map
        freq_map = Counter(nums)

        # build heap
        for num, freq in freq_map.items():
            item = [freq, num]
            heapq.heappush(heap, item)

            if len(heap) > k:
                heapq.heappop(heap)

        #convert heap
        return [num for freq, num in heap]
        '''
        