class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        valid conditions:
        - number of left - number of right = number of start -> doesnt work

        need to catch errors as we go:
        - use stack -> doesnt work
        
        '''
        leftMin = 0
        leftMax = 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else: # "*"
                leftMin -= 1
                leftMax += 1

            if leftMax < 0: # all stars turn to left -> still more right then left -> cannot be closed
                return False
            # leftMax >= 0 -> valid
            if leftMin < 0: # you have enough stars to make it correct 
                leftMin = 0

        return leftMin == 0