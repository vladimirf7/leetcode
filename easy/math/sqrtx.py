"""solved with help, middle """

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x
        while result*result > x:
            result = int((result + x/result) / 2)
        return int(result)

if __name__ == '__main__':
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(5) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(9) == 3