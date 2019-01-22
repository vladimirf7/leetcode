"""solved, middle"""

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A[0]), len(A)
        result = [[None] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                result[j][i] = A[i][j]

        return result


if __name__ == "__main__":
    assert (Solution().transpose([[1,2,3], [4,5,6], [7,8,9]]) ==
                                 [[1,4,7], [2,5,8], [3,6,9]])
    assert (Solution().transpose([[1,2], [3,4], [5,6]]) ==
                                 [[1,3,5], [2,4,6]])