#2017/10/2

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # temp = []
        # if not m:
        #     temp.append(nums2[n - 1:len(nums2)])
        #     temp.reverse()
        #
        # elif not n:
        #     temp.append(nums1[m - 1:len(nums1)])
        #     temp.reverse()
        #
        # elif nums1[len(nums1)-len(nums2)-m] <= nums2[len(nums2)-n]:
        #     temp.append(self.merge(nums1, m - 1, nums2, n))
        #
        # elif nums1[len(nums1)-len(nums2)-m] > nums2[len(nums2)-n]:
        #     temp.append(self.merge(nums1, m, nums2, n - 1))
        #
        # nums1 = temp.reverse()
        # print(nums1)
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

a = Solution()
a.merge([1,3,5,7,9],3,[2,4],2)