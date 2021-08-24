class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n=len(prices)
        
        minimumprice=prices[0]
        maxpro=0
        
        for i in range(0,n):
            minimumprice=min(minimumprice,prices[i])
            
            maxpro=max(maxpro,prices[i]-minimumprice)
            i=i+1
            
        return maxpro
