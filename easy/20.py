

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        brackets = {"{": 0, "}": 0, "(": 0, ")": 0, "[": 0, "]": 0}
        for char in s:
            if char in brackets:
                brackets[char] += 1
        if brackets["{"] != brackets["}"] or brackets["("] != brackets[")"] or brackets["["] != brackets["]"]:
            return False

        while s:
            old_l = len(s)
            for i in range(old_l-1):
                if s[i:i+2] in ("()", "{}", "[]"):
                    s = s[:i]+s[i+2:]
            new_l = len(s)
            if old_l == new_l:
                return False
        return True


if __name__ == '__main__':
    print("ANSWER")
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([])"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("([)"))
    print(Solution().isValid("([)}"))
