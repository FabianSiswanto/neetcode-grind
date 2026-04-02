class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        hashmap -> char: index

        if detect duplicate -> skip l pointer to 1 after dupe index (make sure l go right too)
        update max len, compare to r - l + 1
        
        save to map
        '''
        max_len = 0
        l = 0
        map = {} #char: last index

        for r in range(len(s)):
            cur_char = s[r]

            if cur_char in map:
                potential_l = map[cur_char] + 1 # skip left boundary
                l = max(l, potential_l) # l never shrink
            
            # save to map
            map[cur_char] = r

            cur_len = r - l + 1
            max_len = max(max_len, cur_len)

        return max_len