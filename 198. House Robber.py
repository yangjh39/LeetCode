# 2017/11/1

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            fk2 = nums[0]
            if len(nums) > 1:
                fk1 = max(nums[0], nums[1])
            else:
                fk1 = 0
        else:
            fk1, fk2 = 0, 0

        fk = max(fk1, fk2)

        for i in range(2, len(nums)):
            fk = max(fk1, fk2 + nums[i])
            fk2 = fk1
            fk1 = fk

        return fk

        # last, now = 0, 0
        #
        # for i in nums: last, now = now, max(last + i, now)
        #
        # return now
