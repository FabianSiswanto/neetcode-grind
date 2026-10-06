class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        - window size is len of s1
        - set/ freq counter is same
        
        - loop through all window
        '''
        window_size = len(s1)
        if len(s2) < window_size:
            return False

        need = Counter(s1)
        have = Counter(s2[:window_size])

        if need == have:
            return True

        for r in range(window_size, len(s2)):
            # update counter
            to_add = s2[r]

            l = r - window_size
            to_remove = s2[l]

            have[to_add] += 1
            have[to_remove] -= 1

            # if have[to_remove] == 0:
            #     del have[to_remove]

            # check if match
            if need == have:
                return True

        return False
