# 2017/11/4
import math

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return 2**int(math.log(n) / math.log(2)) == n if n > 0 else False

        # bits
        # return n > 0 and not (n & n - 1)

