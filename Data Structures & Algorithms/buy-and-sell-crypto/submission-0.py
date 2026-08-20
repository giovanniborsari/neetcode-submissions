class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        buy = prices[0]

        for i in range(len(prices)-1):
            if prices[i+1] < buy:
                buy = prices[i+1]
            elif prices[i+1] > buy:
                bestProfit = max(bestProfit,(prices[i+1] - buy))
            else:
                continue
        return bestProfit
            

        