
#To solve we use pointer to update the values we compare

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, Sell = 0,1
        maxp = 0
        
        #len() returns the length of an object, in this case the array 
        while buy < len(prices):
            #checking to see whats profitable 
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                #to determine which profit day is the highest 
                maxp = max(maxp, profit)
            else:
                buy = Sell
            Sell += 1
            
            return maxp
        
        
        # lesson Learn maybe spaces arent needed 
        
        class Solution:
         def maxProfit(self, prices: List[int]) -> int:
            buy,sell=0,1
            maxProfit =0
            while sell<len(prices):
              if (prices[buy]<prices[sell]):
                profit =prices[sell]-prices[buy]
                maxProfit=max(maxProfit, profit)
            else:
                buy=sell
            sell+=1
        return maxProfit