#2017/10/8
from functools import reduce

class Solution(object):
    # def rotation(self, l):
    #     if l.__len__() > 1:
    #         r = []
    #         for i in range(l.__len__()-1):
    #             r.append(l[i]+l[i+1])
    #         return r
    #
    # def generate(self, numRows):
    #     """
    #     :type numRows: int
    #     :rtype: List[List[int]]
    #     """
    #     if numRows == 0:
    #         return []
    #
    #     pt = [[1]]
    #
    #     for i in range(2, numRows + 1):
    #         pt.append([1, temp.rotation(pt[i-2]), 1])
    #
    #     return pt
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            #res += [list(map((lambda x, y: x + y), res[-1] + [0], [0] + res[-1]))]
            res += [[x + y for x, y in zip(res[-1] + [0], [0] + res[-1])]]
        return res[:numRows]

temp = Solution()
temp.generate(3)