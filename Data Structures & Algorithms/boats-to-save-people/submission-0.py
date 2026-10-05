class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # ligtest to heavy
        people.sort()

        # Two pointers: l = lightest remaining, r = heaviest remaining
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1      # lligthest person

            r -= 1 #largest
    

            # One boat used per iteration
            boats += 1

        return boats #Courtesy of Kenneth Santoso. Sini by one leeetcode
        '''
        sort
        
        l and r

        if r > limit -> cannot pair -> move r
        1 2 4 5
        1 2 2 3 3
        '''

