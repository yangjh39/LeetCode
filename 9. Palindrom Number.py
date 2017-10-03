class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        r = int(repr((x >= 0) * x)[::-1])
        return (r < 2 ** 31) and (r == x)

temp = Solution()
temp.isPalindrome(-1)