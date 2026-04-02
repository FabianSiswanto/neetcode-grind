class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        holding
           
         1 2 3 4 5 6
        [7,1,5,3,6,4]
           b s b s
               b
             s
               n
                 i

         1 2 3 4 5
        [1,2,3,4,5]
         b       s
         b
                 s

        lower than s = new_b
        higher than b = s

        execute trade if before b > s
        execuite trade if s = len(prices) - 1

        if new_b > s:
          if b < s:
            profit += s - b
          b = new_b
        '''
        res = 0
        
        for i in range(1, len(prices)):
          if prices[i] > prices[i - 1]:
            res += prices[i] - prices[i - 1]

        return res