#2017/9/26
from functools import reduce

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        num_list = list(num[::-1])

        while n-1:
            next = []
            out = list(num_list.pop())

            while num_list:
                if num_list[-1] == out[-1]:
                    out.append(num_list.pop())
                else:
                    next.append(repr(len(out)))
                    next.append(out[0])
                    out = list(num_list.pop())

            next.append(repr(len(out)))
            next.append(out[0])
            num_list = next[::-1]

            n -=1

        return reduce((lambda x, y: x + y), num_list[::-1])

        #use regular expression
        # s = '1'
        # for _ in range(n - 1):
            # s = ''.join(str(len(group)) + digit
            #             for group, digit in re.findall(r'((.)\2*)', s))

            # s = ''.join(str(len(list(group))) + digit
            #             for digit, group in itertools.groupby(s))

            # s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

        # return s


temp = Solution()
temp.countAndSay(8)
