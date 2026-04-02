class Solution:
    def isValid(self, s: str) -> bool:
        '''
        dictionary of reverse of brackets

        dict of conversion,
        closing bracket: opening

        add stuff, converted
        start pop after direction change, this is the condition you need to check (if not in dict)
        if stuff same pop
        '''

        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c in brackets: # if closing bracket
                if stack and brackets[c] == stack[-1]: #peek
                    stack.pop()
                else:
                    return False
            else: # if opening bracket
                stack.append(c)

        if not stack:
            return True
        else:
            return False
            




        