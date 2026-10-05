class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        sort
        
        l and r

        if r > limit -> cannot pair -> move r
        1 2 4 5
        1 2 2 3 3

        sum l + r <= limit -> l can move
        - r always move
        '''
        people.sort()

        res = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            total = people[l] + people[r]
            if total <= limit:
                l += 1

            r -= 1
            res += 1

        return res
