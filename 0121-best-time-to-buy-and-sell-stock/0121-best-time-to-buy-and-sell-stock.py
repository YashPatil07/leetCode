class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        mini=prices[0]
        
        for i in range(1,len(prices)):
            if prices[i]-mini<0:
                mini=prices[i]
            else:
                result=max(result, prices[i]-mini)
                
        return result