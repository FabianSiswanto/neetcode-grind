class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        keep track of extra open brackets -> use var

        first pass:
        - if ( -> increment var -> append to res
        - if ) and var still available (more than 0) -> append to res, decrement var
        - if normal char -> not ) -> append to res

        second pass -> traverse res in reverse:
        - remove extra open brackets ( till var is 0
        !!! this works because left most ( -> have more chance of finding a ) later, GREEDY !!!
        '''
        extra_opening_count = 0
        res = []

        for c in s:
            if c == "(":
                extra_opening_count += 1
                res.append(c)
            elif c == ")" and extra_opening_count > 0:
                extra_opening_count -= 1
                res.append(c)
            elif c != ")": # normal character
                res.append(c)


        filtered = []
        for c in reversed(res):
            if c == "(" and extra_opening_count > 0:
                extra_opening_count -= 1 # will skip right most (
            else:
                filtered.insert(0, c) # append from left
        
        return "".join(filtered)