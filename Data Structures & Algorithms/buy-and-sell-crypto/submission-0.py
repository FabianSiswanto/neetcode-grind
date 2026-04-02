class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        initialize so that sell is after buy
        initialize profit to 0 (default)

        check if price makes sense (gives profit)
            if yes check if better profit, if yes update
        if price dont make sense, update lower price
        '''
        l = 0
        r = 1
        profit = 0

        while r < len(prices): #lead with r
            if prices[l] < prices[r]:
                cur_profit = prices[r] - prices[l]
                profit = max(profit, cur_profit)
            else:
                l = r
            r += 1
        
        return profit


        