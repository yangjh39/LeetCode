# 2017/11/1

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
            print(nums)


        #Another way is using reverse!(Interesting)

temp = Solution()
temp.rotate([1,2,3,4,5,6,7],3)