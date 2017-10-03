#2017/10/1
from functools import reduce

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # def Dec2Bin(dec):
        #     result = '0'
        #
        #     if dec:
        #         result = Dec2Bin(dec // 2)
        #         return result + str(dec % 2)
        #     else:
        #         return result


        num1 = reduce(lambda x, y: x * 2 + y, [int(i) for i in list(a)])
        num2 = reduce(lambda x, y: x * 2 + y, [int(i) for i in list(b)])
        num = num1 + num2

        return bin(num)[2:]

temp = Solution()
temp.addBinary("0","0")