# 2017/10/19

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

        # dic = {}
        # for i, num in enumerate(numbers):
        #     if target - num in dic:
        #         return [dic[target - num] + 1, i + 1]
        #     dic[num] = i