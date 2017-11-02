# 2017/11/1

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        origin = n

        while n != 1:
            n = sum([pow(int(x), 2) for x in list(str(n))])
            if n == origin:
                return False

        return True

temp = Solution()
temp.isHappy(3)

