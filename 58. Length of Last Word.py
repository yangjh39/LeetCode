#2017/9/30
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not s.strip():
            return 0

        sp = s.split(' ')
        return sp[-1].__len__()

        # return len(s.rstrip(' ').split(' ')[-1])
temp = Solution()
temp.lengthOfLastWord(" a")