#2017/10/11


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h, t = 0, len(s) - 1
        while h < t:
            while h < t and not s[h].isalnum():
                h += 1
            while h < t and not s[t].isalnum():
                t -= 1
            if s[h].lower() != s[t].lower():
                return False
            h += 1
            t -= 1

        return True


