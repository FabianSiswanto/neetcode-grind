class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        brute force -> restart everytime remove stuff
        -> optimize by removal from middle -> continue from there
        -> must be able to remove from middle -> pop -> use stack

        STORE STATE: [char, count]

        check:
        - if same item -> increment count of top
        - if diff item -> append to stack, with count of 1
        - after increment count -> if top item count == k -> pop
        '''
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()

        res = [char * count for char, count in stack]

        return "".join(res)
                
                


        