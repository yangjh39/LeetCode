# 2017/10/20

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        self.dic = {}

        for i, j in enumerate(nums):
            try:
                self.dic[j] += 1
            except KeyError:
                self.dic.update({j:1})

        return [k for k, v in self.dic.items() if v == max(self.dic.values())][0]


#Java Solution
# public class Solution {
#     public int majorityElement(int[] nums) {
#         int candidate = 0;
#         int count = 0;
#         for (int i = 0; i < nums.length; i++) {
#             if (count == 0) {
#                 candidate = nums[i];
#                 count++;
#             } else {
#                 if (nums[i] == candidate) {
#                     count++;
#                 } else {
#                     count--;
#                 }
#             }
#         }
#         return candidate;
#     }
# }

temp = Solution()
temp.majorityElement([3,2,3])