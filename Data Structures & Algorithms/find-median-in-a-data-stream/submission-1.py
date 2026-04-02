class MedianFinder:

    def __init__(self):
        self.small = [] #max heap
        self.large = [] #min heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # check validity condition -> max of small < min of large
        small_and_large_filled = self.small and self.large
        if small_and_large_filled and not -self.small[0] <= self.large[0]:
            item = -heapq.heappop(self.small)
            heapq.heappush(self.large, item)

        # rebalance weight
        if len(self.small) - len(self.large) > 1:
            item = -heapq.heappop(self.small)
            heapq.heappush(self.large, item)
        if len(self.large) - len(self.small) > 1:
            item = -heapq.heappop(self.large)
            heapq.heappush(self.small, item)
                

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            lower = -self.small[0]
            larger = self.large[0]

            return (lower + larger) / 2
        
        