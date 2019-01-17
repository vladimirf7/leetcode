"""solved, easy"""

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        mid = len(A) // 2
        A.sort(key=lambda x: x % 2)

        return [item for sub in zip(A[:mid], A[mid:]) for item in sub]

if __name__ == "__main__":
    assert (Solution().sortArrayByParityII([4, 2, 5, 7]) == [4, 5, 2, 7] or 
            Solution().sortArrayByParityII([4, 2, 5, 7]) == [4, 7, 2, 5] or
            Solution().sortArrayByParityII([4, 2, 5, 7]) == [2, 5, 4, 7]  or
            Solution().sortArrayByParityII([4, 2, 5, 7]) == [2, 7, 4, 5])