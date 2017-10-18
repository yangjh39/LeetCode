#2017/10/11


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []

        result = 0
        for i in range(nums.__len__()):
            result ^= nums[i]

        return result

    # def singleNumber3(self, nums):
    #     return 2 * sum(set(nums)) - sum(nums)