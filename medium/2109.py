from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        prev_i = 0
        for i in spaces:
            words.append(s[prev_i:i])
            prev_i = i
        words.append(s[prev_i:])
        return " ".join(words)

x = Solution().addSpaces("LeetcodeHelpsMeLearn", [8,13,15])
print(x)
