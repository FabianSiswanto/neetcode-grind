class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        starting gas station index -> loop once clockwise
        '''    
        tank = 0
        start = 0

        if sum(cost) > sum(gas):
            return -1

        for i in range(0, len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                # reset
                tank = 0
                start = i + 1

        return start