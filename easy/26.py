from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        u = sorted(list(set(nums)))

        nums[:0] = u

        return len(u)

print(Solution().removeDuplicates([-1,0,0,0,0,3,3]))