class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        have left and right pointer
        make sure each pointer is looking at alphanumeric
        if both pointer not equal -> return false (try to terminate fast)
        increment pointers
        '''
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
        