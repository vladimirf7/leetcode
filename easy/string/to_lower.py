"""solved, easy"""

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        SHIFT = 32
        result = []

        for char in str:
            result.append((chr(ord(char) + SHIFT)) if "A" <= char <= "Z" else char)
        
        return "".join(result)

if __name__ == "__main__":
    assert Solution().toLowerCase("Hello") == "hello"
    assert Solution().toLowerCase("hello") == "hello"
    assert Solution().toLowerCase("HELLO") == "hello"