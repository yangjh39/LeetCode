#2017/9/23

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # import pandas as pd
        # split_strs = pd.DataFrame([list(x) for x in strs])
        #
        # for i in list(split_strs.columns):
        #     if not (split_strs == split_strs.loc[0, i]).all()[i]:
        #         break
        #
        # return strs[0][0:i]

        # if len(strs) <= 1:
        #     try:
        #         return strs[0]
        #     except IndexError:
        #         return ""
        #
        # import numpy as np
        # split_strs = [list(x) for x in strs]
        #
        # for i in np.arange(len(split_strs)):
        #     split_strs[i] = split_strs[i][0:min([len(x) for x in split_strs])]
        #
        # ind = 0; count = 0; no = 0
        # for ind, l in enumerate([len(a) for a in [set(x) for x in np.stack(split_strs,1).tolist()]]):
        #     count += 1
        #     if l != 1:
        #         no += 1
        #         break
        #
        # return strs[0][0:count - no]
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

temp = Solution()
temp.longestCommonPrefix(['aab', 'aa'])

