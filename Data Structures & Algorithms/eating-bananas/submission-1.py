class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        try new k val
        validate:
            go over all pile
                hours += ceil(pile / k)

        k start at 1
        upper bound is max of piles
        binary search down to find smallest k that is valid
        '''
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            m = (l + r) // 2
            cur_h = 0
            for p in piles:
                cur_h += math.ceil(p / m)
            
            if cur_h <= h:
                res = m
                # go left
                r = m - 1
            else:
                # go right
                l = m + 1

        return res
        