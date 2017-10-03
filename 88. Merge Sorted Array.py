class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        if not m:
            temp.append(nums2[n - 1:len(nums2)])
        if not n:
            temp.append(nums1[m - 1:len(nums1)])

        if nums1[len(nums1) - m] < nums2[len(nums2) - n]:
            temp.append(self.merge(nums1, m - 1, nums2, n))
        if nums1[len(nums1) - m] > nums2[len(nums2) - n]:
            temp.append(self.merge(nums1, m, nums2, n - 1))