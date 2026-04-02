class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        - while new_start > prev_end -> append old items 
        - while new_end >= prev_start -> update new interval (min_start, max_end)
            -> append new interval
        - while not cover all old intervals -> append remaining
        '''
        n = len(intervals)
        i = 0

        res = []

        new_start = newInterval[0]
        # do nothing while new start > cur end
        while i < n and new_start > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        # insert new interval -> after prev cur, before next cur
        # while overlap -> new end >= cur start
        while i < n and not intervals[i][0] > newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            
            i += 1
        res.append(newInterval)

        while i < n: # need to append everything from old item
            res.append(intervals[i])
            i += 1

        return res