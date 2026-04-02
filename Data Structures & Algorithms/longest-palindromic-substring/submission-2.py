class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        try spread out from each index -> update if higher len
        - handle odd and even case

        res_start_i
        res_len
        '''
        res_start_i = 0
        res_len = 0

        for i in range(len(s)):
            # odd case
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > res_len:
                    res_len = cur_len
                    res_start_i = l
                l -= 1
                r += 1

            # even case
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > res_len:
                    res_len = cur_len
                    res_start_i = l
                l -= 1
                r += 1

        return s[res_start_i: res_start_i + res_len]