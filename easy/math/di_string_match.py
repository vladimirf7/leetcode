"""solved, easy, beats 99.95%"""

class Solution:
    def diStringMatch(self, S):
        """
        Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

        Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

        If S[i] == "I", then A[i] < A[i+1]
        If S[i] == "D", then A[i] > A[i+1]

        :type S: str
        :rtype: List[int]
        """
        result = []
        start, stop = 0, len(S)

        for char in S:
            if char == "I":
                result.append(start)
                start += 1
            else:
                result.append(stop)
                stop -= 1
        if char == "I":
            result.append(start)
        else:
            result.append(stop)

        return result



if __name__ == "__main__":
    assert Solution().diStringMatch("IDID") == [0,4,1,3,2]
    assert Solution().diStringMatch("III") == [0,1,2,3]
    assert Solution().diStringMatch("DDI") == [3,2,0,1]