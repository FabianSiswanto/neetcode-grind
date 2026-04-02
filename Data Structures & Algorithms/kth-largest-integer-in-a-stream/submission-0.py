class KthLargest:
    '''
    max heap

    pop k times -> temp

    store all at list, except last one k = 0

    return temp after

    max heap -> pop k times
    3
    3 3 2
    1

    min heap -> pop till len(heap) = k -> keep it at this state at all times
    5 6 7



    '''

    # def __init__(self, k: int, nums: List[int]):
    #     # init heap
    #     min_heap = []

    #     for i in len(nums):
    #         if i <= k:
    #             heapq.heappush(min_heap, nums[i])
    #         else:
    #             self.add(self.minHeap, nums[i])
            

        

    # def add(self, val: int) -> int:
    #     # pop

    #     # add

    #     # peek

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
