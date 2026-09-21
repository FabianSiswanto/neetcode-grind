class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        1. build prefix table
        have prev and cur
        if item at prev and cur match
            -> set lps as prev + 1
            -> update prev and cur

        if prev at 0 -> cant move prev no more
            -> lps is 0 
            -> update cur only

        else -> move prev to the lps of prev-1

        2. actual part
        if match -> update both indexes

        if j is 0 -> look at next haystack char -> move i
        if j is not 0 -> update j to prev j (j - 1)'s lps

        if j is len -> return
        '''
        # build lps
        lps = [0] * len(needle)
        prev, cur = 0, 1

        while cur < len(needle):
            if needle[cur] == needle[prev]:
                lps[cur] = prev + 1 # prev length + 1
                prev += 1
                cur += 1
            elif prev != 0:
                prev = lps[prev - 1] # todo: understand
            else: # prev at 0
                lps[cur] = 0
                cur += 1

        i = 0 # idx of haystack
        j = 0 # idx of needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1] # todo: understand
            else:
                i += 1 #only update haystack index once exhaust all j
            
            if j == len(needle): # needle out of bounds
                return i - len(needle)

        return -1