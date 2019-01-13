"""solved with help, middle"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_ = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for char in s:
            if char in dict_.values():
                stack.append(char)
            elif char in dict_:
                if stack == [] or dict_[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

        

if __name__ == "__main__":
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("{[]}") == True