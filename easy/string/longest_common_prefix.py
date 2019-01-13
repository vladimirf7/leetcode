"""solved, easy"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_str = min([len(x) for x in strs] or [0])
        result = []

        for i in range(min_str):
            if len({string[i] for string in strs}) == 1:
                result.append(strs[0][i])
            else:
                break
        return "".join(result)

if __name__ == "__main__":
    # Solution().longestCommonPrefix(["flower","flow","flight"])
    assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
    assert Solution().longestCommonPrefix(["pig", "pigeon", "piggy"]) == "pig"