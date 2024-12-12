from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            gifts.sort()
            gifts[-1] = int(gifts[-1]**0.5)
            print(gifts)
            k += -1
        res = sum(gifts)
        print(res)
        return res


s = Solution()
s.pickGifts([25,64,9,4,100], 4)
