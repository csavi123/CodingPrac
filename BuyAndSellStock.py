class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left=0
        right=1
        maxProfit=0
        while right<len(prices):
            if prices[left] < prices[right]:
                profit=prices[right]-prices[left]
                maxProfit=max(profit,maxProfit)
            else:
                left=right
            right+=1
        return maxProfit
solution = Solution()
print(solution.maxProfit([5,1,5,6,7,1,10]))  # 49