"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        - sort intervals -> by start date
        - last end -> first interval.end
        - go over each one from second interval -> if there is overlap -> increment num_rooms
            - if last end > cur.start -> overlap -> update last end = cur.end
        '''
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda interval: interval.start)
        ends_min_heap = []

        for interval in intervals:
            if ends_min_heap and ends_min_heap[0] <= interval.start:
                heapq.heappop(ends_min_heap) #remove finished meeting end time

            #basically use same room, with new end time
            heapq.heappush(ends_min_heap, interval.end)
        return len(ends_min_heap)
        