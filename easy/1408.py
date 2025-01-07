from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        lword = len(words)
        r = set()
        for i in range(lword-1):
            for j in range(i+1, lword):
                if words[i] in words[j]:
                    r.add(words[i])
                    break

        return list(r)
