# 2017/10/28
from functools import reduce


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = -2
        m = 1
        last = chars[0]

        for i in range(1, len(chars)):
            now = chars[i]

            if last == now:
                m += 1
            else:
                n += 2
                chars[n] = last
                if m > 1:
                    if m >= 10:
                        w = len(str(m))
                        for j in range(w):
                            chars[n + j + 1] = str(m)[j]
                        n = n + w - 1
                    else:
                        chars[n + 1] = str(m)
                else:
                    n -= 1
                last = now
                m = 1

        if m != 0:
            n += 2
            chars[n] = last
            if m > 1:
                if m >= 10:
                    w = len(str(m))
                    for p in range(w):
                        chars[n + p + 1] = str(m)[p]
                    n = n + w - 1
                else:
                    chars[n + 1] = str(m)
            else:
                n = n - 1

        return n + 2

temp = Solution()
temp.compress(['a','b','c'])
