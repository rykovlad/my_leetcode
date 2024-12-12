from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums = sorted(nums)
        for i, x in enumerate(nums):
            if x == target:
                print(nums)
                return i


s = Solution()
s.searchInsert([1,3,5,6], 2)