class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        pointer for all strings -> index based -> loop per index
        -> if all pointers same -> loop through all words -> if same -> append

        fail:
        - out of bounds
        - dont match

        use first item as reference
        '''
        reference = strs[0]
        for i in range(len(reference)):
            for s in strs[1:]:
                if i >= len(s) or reference[i] != s[i]:
                    return s[:i]

        return reference

            