class Solution:
    def decodeString(self, s: str) -> str:
        '''
        start from most inner

        use stack -> stop when u find a closing bracket -> set word -> until find an opening
            -> multiply by number
        stack -> state -> cur str, k

        if number -> handle multiple digits -> multiple old one by 10, add new one

        if [ -> save state, reset current state

        if ] -> restore state from stack, update the 
        '''
        stack = []
        cur_str = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = int(c) + k * 10

            elif c == "[":
                cur_state = [cur_str, k]
                stack.append(cur_state)

                # reset state
                cur_str = ""
                k = 0

            elif c == "]":
                prev_str, cur_k = stack.pop() # figure out where cur_k is from

                cur_str = prev_str + cur_k * cur_str

            else: # normal character
                cur_str += c

        return cur_str

        