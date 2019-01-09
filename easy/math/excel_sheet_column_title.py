"""solved with help, hard """

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n > 0:
            n -= 1
            result.append(chr(n % 26 + 65))
            n = n // 26

        return ''.join(result[::-1])

if __name__ == '__main__':
    assert Solution().convertToTitle(1) == 'A'
    assert Solution().convertToTitle(28) == 'AB'
    assert Solution().convertToTitle(701) == 'ZY'