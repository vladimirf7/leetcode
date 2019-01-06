"""solved, easy"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                del nums[j]
            i += 1
            j += 1
        return len(nums)


if __name__ == '__main__':
    assert Solution().removeDuplicates([1, 1, 2]) == 2
    assert Solution().removeDuplicates([1, 2, 3, 3, 3, 4, 5, 5, 6]) == 6
    assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    assert Solution().removeDuplicates([1, 1]) == 1