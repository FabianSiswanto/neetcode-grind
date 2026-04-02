class MedianFinder:

    def __init__(self):
        self.small = [] #max heap
        self.large = [] #min heap
        

    def addNum(self, num: int) -> None:
        condition = self.large and num > self.large[0]
        if condition:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

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
        
        