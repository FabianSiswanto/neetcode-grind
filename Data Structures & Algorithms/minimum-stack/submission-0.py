class MinStack:
    '''
    cannot use heap -> not constant time
    cannot use min variables (need counter) -> compare when pop -> dont know next min
    
    stack: val, min_so_far
    '''

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        '''
        if stack empty -> set min as self val -> append

        peek -> to get previous min -> update if needed -> append
        '''
        if not self.stack:
            item = (val, val)
            self.stack.append(item)
            return

        # already have item
        _, prev_min = self.stack[-1]
        cur_min = min(prev_min, val)

        item = (val, cur_min)
        self.stack.append(item)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val, _ = self.stack[-1]

        return val
        

    def getMin(self) -> int:
        _, cur_min = self.stack[-1]
        
        return cur_min
        
