"""solved, easy, beats 92%"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        A self-dividing number is a number that is divisible by every
        digit it contains.

        For example, 128 is a self-dividing number because 128 % 1 == 0,
        128 % 2 == 0, and 128 % 8 == 0.

        Also, a self-dividing number is not allowed to contain the digit zero.

        Given a lower and upper number bound, output a list of every possible
        self dividing number, including the bounds if possible.

        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []

        for n in range(left, right+1):
            if "0" in str(n):
                continue
            is_self_divisable = True
            for x in str(n):
                if n % int(x):
                    is_self_divisable = False
                    break
            if is_self_divisable:
                result.append(n)

        return result


if __name__ == "__main__":
    assert (Solution().selfDividingNumbers(1, 22) ==
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])