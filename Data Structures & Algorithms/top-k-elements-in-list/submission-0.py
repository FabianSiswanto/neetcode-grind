class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        freq map

        keep heap of size k
        heap store [frequency, number]
        '''
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

        