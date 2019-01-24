"""solved with help, easy"""

class Solution:
    def binaryGap(self, N):
        """
        Given a positive integer N, find and return the longest distance
        between two consecutive 1's in the binary representation of N.
        If there aren't two consecutive 1's, return 0.

        :type N: int
        :rtype: int
        """
        one_indices = [i for i, item in enumerate(bin(N)) if item == "1"]
        
        return max([y - x for x, y in zip(one_indices, one_indices[1:])] or [0])



if __name__ == "__main__":
    assert Solution().binaryGap(22) == 2
    assert Solution().binaryGap(5) == 2
    assert Solution().binaryGap(6) == 1
    assert Solution().binaryGap(8) == 0