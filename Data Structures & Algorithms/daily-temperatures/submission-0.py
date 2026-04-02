class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        res[i] = distance to next warmer day, if doesnt exist set to 0
            distance = warmer_ i - i

        take action when find warmer day -> store when find same or cooler day
        -> MONOTONIC DECREASING STACK storing (i, temp)

        cannot keep track of warmest day -> doesnt work as we only need warmer
        '''
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i, temp in enumerate(temperatures):
            # take action when cur item is warmer than stack top
            while stack and stack[-1][1] < temp:
                stack_i, stack_temp = stack.pop()

                distance = i - stack_i
                res[stack_i] = distance

            stack.append([i, temp])


        return res