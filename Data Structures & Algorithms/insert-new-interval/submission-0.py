class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        - merge overlapping intervals

        prev and after variables
        find interval spot -> loop till -> 

        cases:
            - prev new after
            - merge after
            - prev merge
            - merge

        prev new after
        check if need to merge those three -> check twice
        - start with prev -> if prev.end > new.start -> merge prev.start, max(new.end, prev.end)
        - 
        merge ->

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
        # need to merge if new_end >= prev_start
        while prev_idx < n and newInterval[1] >= intervals[prev_idx][0]:
            newInterval[0] = min(intervals[prev_idx][0], newInterval[0])
            newInterval[1] = max(intervals[prev_idx][1], newInterval[1])
            
            prev_idx += 1
        res.append(newInterval)

        while prev_idx < n: # need to append everything from old item
            res.append(intervals[prev_idx])
            prev_idx += 1

        return res