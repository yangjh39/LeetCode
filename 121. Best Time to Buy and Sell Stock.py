#2017/10/9

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if prices.__len__()<2:
        #     return 0
        #
        # b = prices.pop(0)
        #
        # while prices[0]<=b:
        #     b = prices.pop(0)
        #     if prices.__len__() == 0:
        #         break
        #
        # if prices:
        #     return max(max([(x - b) for x in prices]), self.maxProfit(prices))
        # else:
        #     return 0

        #Greedy Algorithm!!!
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

    #multi - transactions
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #
    #     max_profit, min_price = 0, float('inf')
    #
    #     for price in prices:
    #         min_price = min(min_price, price)
    #         profit = price - min_price
    #
    #         if profit > 0:
    #             max_profit += profit
    #             min_price = price
    #
    #     return max_profit

temp = Solution()
temp.maxProfit([7, 1, 2, 3])
