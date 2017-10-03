#2017/9/23

import  numpy as np

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # maximum = 2**31-1
        # split_array_max = np.array([int(a) for a in list(str(maximum))])
        # split_array_x = np.array([int(a) for a in list(str(x))])
        #
        # if split_array_x.__len__()==1:
        #     return x
        #
        # split_array_reverse = split_array_x[-np.arange(1,split_array_x.__len__()+1)]
        #
        # start = 0
        #
        # for i, num in enumerate(split_array_reverse):
        #     if num == 0:
        #         start = i+1
        #     else:
        #         break
        #
        # split_array_reverse_del0 = split_array_reverse[start:]
        # if len(split_array_reverse_del0)>len(split_array_max):
        #     return 0
        # elif len(split_array_reverse_del0)==len(split_array_max):
        #     e = split_array_max[split_array_reverse_del0!=split_array_max][0]
        #     f = split_array_reverse_del0[split_array_reverse_del0!=split_array_max][0]
        #     if e<f:
        #         return 0
        # else:
        #     num = 0
        #     for i in np.arange(len(split_array_reverse_del0)):
        #         num += split_array_reverse_del0[i]*(10**(len(split_array_reverse_del0)-i-1))
        #
        #     return num


        s=int(x>=0);r=int(repr(s*x)[::-1]);return(r<2**31)*s*r

temp = Solution()
temp.reverse(75847891247981212935100)