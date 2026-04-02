class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        sort -> start
        greedy algo -> delete item if cause overlap -> increment res -> keep prev there

        1,2 1,4 2,4
        '''
        res = 0
        if len(intervals) == 1:
            return res

        intervals.sort(key = lambda i: i[0])
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            overlap = prev_end > start

            if overlap:
                res += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return res