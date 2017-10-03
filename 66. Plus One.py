#2017/9/30
from functools import reduce
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits[-1] += 1
        # for i in range(1, len(digits)+1):
        #     if digits[-i] == 10:
        #         digits[-i] = 0
        #         if i < len(digits):
        #             digits[-(i+1)] += 1
        #         else:
        #             digits.reverse()
        #             digits.append(1)
        #             digits.reverse()
        #     else:
        #         break
        #
        # return digits
        num=reduce(lambda x,y:x*10+y,digits)+1
        return [int(i) for i in str(num)]

temp = Solution()
temp.plusOne([1,4,6])
