"""solved, easy"""

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        a, b = 0, 1

        for i in range(N-1):
            a, b = b, a+b

        return b


if __name__ == "__main__":
    assert Solution().fib(0) == 0
    assert Solution().fib(1) == 1
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    assert Solution().fib(5) == 5
    assert Solution().fib(6) == 8
    assert Solution().fib(7) == 13