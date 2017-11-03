# 2017/11/2

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # total = 0
        #
        # for j in range(2, n):
        #     print(j)
        #     i = 1
        #     num = 0
        #
        #     while i <= pow(j, 0.5):
        #         if j % i == 0:
        #             num += 1
        #         i += 1
        #
        #     if num == 1:
        #         total += 1
        #
        # return total if n > 2 else 0

        class Solution:
            def countPrimes(self, n):
                """
                :type n: int
                :rtype: int
                """
                if n < 3:
                    return 0

                prime = [True] * n
                prime[:2] = [False] * 2

                for i in range(2, int(pow(n - 1, 0.5) + 1)):
                    if prime[i]:
                        #if i is prime, n*i is not prime, n = 2,3,4,5...
                        prime[i * i::i] = [False] * len(prime[i * i::i])

                return sum(prime)


temp = Solution()
temp.countPrimes(5)