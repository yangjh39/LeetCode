# 2017/10/20
from functools import reduce

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = list(s)
        s.reverse()
        index = range(0, len(s))
        d = [26] * len(s)

        return sum(map(lambda x, y: x*y, [ord(x)-64 for x in s], list(map(pow, d, index))))

temp = Solution()
temp.titleToNumber('BA')