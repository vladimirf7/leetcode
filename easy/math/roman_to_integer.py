"""solved with help, hard"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        prev, sum = 0, 0

        for x in s[::-1]:
            if num_map[x] < prev:
                sum -= num_map[x]
            else:
                sum += num_map[x]
            prev = num_map[x]
        return sum


if __name__ == '__main__':
    assert Solution().romanToInt('III') == 3
    assert Solution().romanToInt('IV') == 4
    assert Solution().romanToInt('IX') == 9
    assert Solution().romanToInt('LVIII') == 58
    assert Solution().romanToInt('MCMXCIV') == 1994