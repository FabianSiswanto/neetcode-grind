class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        let a, b
        1. base case for size 1
        3. sort by a_0, b_0
        5. while i < len(interval)
            1. let i be current, j be prev
            2. if a_1 > b_0 -> keep (a_0, b_1) -> modify i_0 with prev_0
            3. increment i if no modification done
        '''
        if len(intervals) == 1:
            return intervals

        # sort by first index
        intervals.sort(key=lambda pair: pair[0])

        i = 1
        while i < len(intervals):
            prev = i - 1
            if intervals[prev][1] >= intervals[i][0]:
                intervals[i][0] = intervals[prev][0]
                intervals[i][1] = max(intervals[i][1], intervals[prev][1])

                del intervals[prev]
            else:
                i += 1

        return intervals