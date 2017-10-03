#2017/9/26

import numpy as np
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums_arr = np.array(nums)
        # if target in nums_arr:
        #     return np.where(nums_arr == target)[0][0]
        # else:
        #     nums_arr = np.append(nums_arr, target)
        #     return np.where(np.sort(nums_arr) == target)[0][0]
        # if len(nums) == 1:
        #     if nums[0]>=target:
        #         return 0
        #     else:
        #         return 1

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if target < nums[mid]:
                high = mid - 1
                print(high)
            elif target > nums[mid]:
                low = mid + 1
                print(low)
            else:
                return mid
        if nums[mid]>target:
            return mid
        else:
            return mid+1

temp = Solution()
temp.searchInsert([1],2)