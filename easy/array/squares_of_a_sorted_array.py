"""solved, easy"""


class Solution:
    def sortedSquares(self, A):
        """
        Given an array of integers A sorted in non-decreasing order,
        return an array of the squares of each number, also in sorted
        non-decreasing order.

        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([n*n for n in A])

if __name__ == "__main__":
    assert Solution().sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert Solution().sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]