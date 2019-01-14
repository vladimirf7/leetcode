"""solved, easy"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        i, j = 0, len(result) - 1

        while i < j:
            result[i], result[j] = result[j], result[i]
            i += 1
            j -= 1

        return "".join(result)


if __name__ == "__main__":
    assert Solution().reverseString("hello") == "olleh"
    assert Solution().reverseString("A man, a plan, a canal: Panama") == "amanaP :lanac a ,nalp a ,nam A"