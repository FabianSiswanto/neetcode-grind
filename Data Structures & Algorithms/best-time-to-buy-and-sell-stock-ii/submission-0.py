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
        b, new_b, s = 0, 0, 0

        for i in range(len(prices)):
          if prices[i] > prices[s]:
            s = i
          if prices[i] < prices[s]:
            new_b = i
          if new_b > s:
            if prices[s] > prices[b]:
              res += prices[s] - prices[b]
            b = new_b
            s = new_b
          

        if prices[s] > prices[b]:
          res += prices[s] - prices[b]

        return res