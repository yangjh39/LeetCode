# 2017/10/20
from functools import reduce

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        if not n:
            return ''

        self.stack = []

        l = n

        while l:
            # r = l % 26
            # if r == 0:
            #     self.stack += [26]
            #     l = l // 26 - 1
            # else:
            #     self.stack += [r]
            #     l = l // 26
            self.stack += [(l-1) % 26]
            l = (l-1) // 26

        self.stack.reverse()
        # return reduce(lambda x, y: str(x)+str(y), [chr(x + 65) for x in self.stack[::-1]])
        return ''.join(self.stack)

temp = Solution()
temp.convertToTitle(26)