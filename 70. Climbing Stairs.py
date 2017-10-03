#2017/10/1
from scipy.special import comb

class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # def cc(x, y):
        #     mul = 1
        #     div = 1
        #
        #     for j in range(1, y + 1):
        #         mul *= (x - j + 1)
        #         div *= j
        #
        #     return mul / div
        #
        # num_2step = n//2
        #
        # num = 0
        # for i in range(1, num_2step+1):
        #     num += cc(n-i, i)
        #
        # return int(num+1)

        """
        One can reach i​th step in one of the two ways:
        Taking a single step from (i−1)th step.
        Taking a step of 22 from (i−2)th step.

        So, the total number of ways to reach ith step is equal to sum of ways 
        of reaching (i−1)​th step and ways of reaching (i−2)​th step.
        """
        if n == 1:
            return 1

        num = list()
        num.append(1)
        num.append(2)

        for i in range(2, n):
            num.append(num[i-1] + num[i-2])

        return num[-1]

temp = Solution()
temp.climbStairs(3)



