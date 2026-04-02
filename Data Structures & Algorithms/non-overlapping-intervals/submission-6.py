class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        sort -> start
        greedy algo -> if overlap -> keep item that ends faster
            -> more room for future intervals -> greedy stays ahead
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