class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        find div -> multiply div till while its not greater than x

        l -> x // 10
        r -> x // div

        chop off left -> x % div
        chop off right -> x / 10

        update div -> since we chop off 2 digits -> divide by 100

        if we chop off enough -> x will be 0 -> loop stops
        '''
        div = 1

        # stop before gets too big -> look forward -> div * 10
        while x >= div * 10:
            div *= 10

        while x:
            l = x % 10
            r = x // div

            if l != r:
                return False
            
            # chop left
            x = x % div
            # chop right
            x = x // 10

            div = div // 100

        return True

        