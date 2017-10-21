# 2017/10/20

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        ind = 1
        num = 0
        f = pow(5, ind)

        while f <= n:
            ind += 1
            num += n//f
            f = pow(5, ind)

        return num
