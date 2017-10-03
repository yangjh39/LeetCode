#2017/9/25
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        new = 0
        for i in range(1, len(nums)):
            if nums[new] != nums[i]:
                new += 1
                nums[new] = nums[i]

        return new + 1

temp = Solution()
temp.removeDuplicates([1,1,2])