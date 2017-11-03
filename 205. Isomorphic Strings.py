# 2017/11/2

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        n = 1
        for i, j in enumerate(list(s)):
            try:
                dic[j] + 1
            except KeyError:
                dic.update({j: n})
                n += 1

        snum = [dic[x] for x in list(s)]

        dic = {}
        n = 1
        for i, j in enumerate(list(t)):
            try:
                dic[j] + 1
            except KeyError:
                dic.update({j: n})
                n += 1

        tnum = [dic[x] for x in list(t)]

        return snum == tnum

        # return [s.find(i) for i in s] == [t.find(j) for j in t]
        # return map(s.find, s) == map(t.find, t)

temp = Solution()
temp.isIsomorphic("abcd", "rrty")