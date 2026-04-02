class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        use stack
        new item after group of slashes found
        if .. -> delete previous item
            if nothing to pop, do nothing
        if . -> do nothing
        combine everything -> start with /, seperated with /
        '''
        stack = []
        cur = ""

        for p in path:
            if p != "/":
                cur += p
                continue

            if cur == ".." and stack:
                stack.pop()

            if cur == "..":
                cur = ""
                continue

            if cur == ".":
                cur = ""
                continue
            
            if len(cur) > 0:
                stack.append(cur)
            cur = ""

        if cur == ".." and stack:
            stack.pop()

        if len(cur) > 0 and cur != "." and cur != "..":
            stack.append(cur)
           
        res = "/" + "/".join(stack)

        print(stack)

        return res

        # for i in stack:

