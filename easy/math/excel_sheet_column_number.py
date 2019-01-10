"""solved, hard"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        reversed = s[::-1]

        for i in range(len(reversed)):
            multiplier = ord(reversed[i]) - 64
            num += 26 ** i * multiplier if i else multiplier

        return num

if __name__ == '__main__':
    assert Solution().titleToNumber('A') == 1
    assert Solution().titleToNumber('Z') == 26
    assert Solution().titleToNumber('AA') == 27
    assert Solution().titleToNumber('BA') == 53
    assert Solution().titleToNumber('ZZ') == 702
    assert Solution().titleToNumber('AAA') == 703