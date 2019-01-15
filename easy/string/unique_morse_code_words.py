"""solved, easy"""


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        SHIFT = 97
        unique_codes = set()
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
                 ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--",
                 "-..-", "-.--", "--.."]

        for word in words:
            unique_codes.add("".join([codes[ord(x)-SHIFT] for x in word]))

        return len(unique_codes)


if __name__ == "__main__":
    assert Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2
    assert Solution().uniqueMorseRepresentations(
        ["rwjje", "aittjje", "auyyn", "lqtktn", "lmjwn"]) == 1
