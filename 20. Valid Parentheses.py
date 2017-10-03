#2017/9/24

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        standard = dict(zip(['(',')','[',']','{','}'],[1,2,4,5,7,8]))
        if s.__len__() >= 2:
            s_num = [standard[x] for x in list(s)]
        else:
            return False

        out = [s_num.pop()]
        while s_num:
            spop = s_num.pop()
            if out:
                if out[-1] - spop == 1:
                    out.pop()
                else:
                    out.append(spop)
            else:
                out.append(spop)

        if out:
            return False
        else:
            return True

temp = Solution()
temp.isValid('({}[])')

