class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        scan from right to left of s
        
        keep track of last number -> prev
        what to do with each number:
        - add cur
        - subtract cur -> prev is larger than cur:
            - prev is (v or x) and cur is I
            - prev is (l or c) and cur is x
            - prev is (d and m) and cur is c
        '''
        symbol_to_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev = -float("inf")
        res = 0
        for c in reversed(s):
            cur = symbol_to_val[c]
            
            if prev > cur: # custom case where we need to subtract
                res -= cur
            else: # regular case
                res += cur
                
            prev = cur

        return res


