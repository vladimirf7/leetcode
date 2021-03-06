"""solved with help, middle"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plusOne([1, 9]) == [2, 0]
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]