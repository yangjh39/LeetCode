#2017/9/25

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        new = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[new] = nums[i]
                new += 1

        return new