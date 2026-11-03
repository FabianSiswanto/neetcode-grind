class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        start with l = 1, r = max of all piles

        try with m -> if valid (cur_h <= h) -> try reduce speed -> go left
        ! think of case when cur_h == h -> also need to update res
        ! think of case when l == r -> 

        if invalid -> must increase -> go right

        ! not enough hours to go through all piles -> h > len(piles)
        -> guaranteed alr in the constraints
        '''
        l = 1
        r = max(piles)

        res = r

        def helper(speed):
            hours = 0

            for pile in piles:
                hour_per_pile = math.ceil(pile / speed)
                hours += hour_per_pile

            return hours


        while l <= r:
            m = (l + r) // 2
            cur_h = helper(m)
            
            valid_speed = cur_h <= h
            if valid_speed:
                res = m
                # try slower speed -> go left
                r = m - 1
            else:
                # must increase speed -> go right
                l = m + 1
        return res
