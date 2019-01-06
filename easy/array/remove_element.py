'''solved, super easy'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)

if __name__ == '__main__':
    assert Solution().removeElement([3, 2, 2, 3], 3) == 2
    assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5