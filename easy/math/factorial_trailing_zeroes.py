"""solved, middle"""
import math


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        result = 0
        mult = math.floor(math.log(n, 5))

        for i in range(1, mult+1):
            result += n//5**i

        return result

if __name__ == '__main__':
    assert Solution().trailingZeroes(0) == 0
    assert Solution().trailingZeroes(4) == 0
    assert Solution().trailingZeroes(5) == 1
    assert Solution().trailingZeroes(7) == 1
    assert Solution().trailingZeroes(10) == 2
    assert Solution().trailingZeroes(30) == 7
    assert Solution().trailingZeroes(200) == 49
