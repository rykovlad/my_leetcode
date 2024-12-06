

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(len(haystack)):
                if needle == haystack[i:i+len(needle)]:
                    return i
        else:
            return -1



s = Solution()
r = s.strStr("leetcode", "code")
print(r)