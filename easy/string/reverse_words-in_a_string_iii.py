"""solved, easy"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([''.join(reversed(w)) for w in s.split()])

if __name__ == "__main__":
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"