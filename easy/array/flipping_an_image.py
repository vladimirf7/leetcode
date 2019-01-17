"""solved, easy"""

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            i, j = 0, len(row)-1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
            for n in range(len(row)):
                row[n] = 1 if row[n] == 0 else 0
                
        return A

if __name__ == "__main__":
    Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
    assert (Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) ==
        [[1,0,0],[0,1,0],[1,1,1]])