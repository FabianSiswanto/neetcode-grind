class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        - while new_start > prev_end -> append old items 
        - while new_end >= prev_start -> update new interval (min_start, max_end)
            -> append new interval
        - while not cover all old intervals -> append remaining
        '''
        n = len(intervals)
        prev_idx = 0

        res = []

        new_start = newInterval[0]
        # do nothing while new start > prev_interval end
        while prev_idx < n and new_start > intervals[prev_idx][1]:
            res.append(intervals[prev_idx])
            prev_idx += 1

        # insert new interval
        # need to merge if overlap -> new_end >= prev_start -> prev_start <= new_end -> not prev_start > new_end
        while prev_idx < n and not intervals[prev_idx][0] > newInterval[1]:
            newInterval[0] = min(intervals[prev_idx][0], newInterval[0])
            newInterval[1] = max(intervals[prev_idx][1], newInterval[1])
            
            prev_idx += 1
        res.append(newInterval)

        while prev_idx < n: # need to append everything from old item
            res.append(intervals[prev_idx])
            prev_idx += 1

        return res