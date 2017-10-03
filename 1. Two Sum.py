#2017/9/22

import  numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        npnums = np.array(nums)
        leave = target - npnums
        temp = set(nums).intersection(set(leave))
        if len(temp)==1:
            b_index = np.where(npnums == np.array(list(temp)))[0].tolist()
            return b_index
        else:
            a_index = np.where(npnums == np.array(min(list(temp))))[0].tolist()
            b_index = np.where(npnums == np.array(max(list(temp))))[0].tolist()
            return [a_index[0],b_index[0]]

        #The following solution has some problems such as the input are [3,2,3],6
        # numbers = dict((number, index) for (index, number) in enumerate(nums))
        # return list(index for (number, index) in numbers.items() if number * 2 != target and target - number in numbers.keys())

temp = Solution()
temp.twoSum([3,2,3],6)
temp.twoSum([3,2,4],5)