from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = ""
        for i in digits:
            d += str(i)
        d = int(d)
        d += 1
        d = str(d)
        return [int(s) for s in d]
