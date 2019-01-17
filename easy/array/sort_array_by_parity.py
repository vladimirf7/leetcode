""""""

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []

        for num in A:
            if num % 2:
                result.append(num)
            else:
                result.insert(0, num)

        return result

if __name__ == "__main__":
    assert (Solution().sortArrayByParity([3,1,2,4]) == [2, 4, 3, 1] or
            Solution().sortArrayByParity([3,1,2,4]) == [4, 2, 3, 1] or
            Solution().sortArrayByParity([3,1,2,4]) == [2, 4, 1, 3] or
            Solution().sortArrayByParity([3,1,2,4]) == [4, 2, 1, 3])