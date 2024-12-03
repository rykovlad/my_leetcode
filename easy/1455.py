class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent = sentence.split()
        i = 1
        for w in sent:
            if searchWord == w[:len(searchWord)]:
                return i
            i += 1
        return -1




x = Solution().isPrefixOfWord("asd asdas asdsdasda 123", "1")
print(x)