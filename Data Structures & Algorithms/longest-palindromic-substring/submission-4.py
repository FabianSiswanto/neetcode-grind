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

        def expand(l: int, r: int) -> None:
            nonlocal res_start_i, res_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > res_len:
                    res_len = cur_len
                    res_start_i = l
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd case
            expand(i, i)
            # even case
            expand(i, i + 1)

        return s[res_start_i: res_start_i + res_len]