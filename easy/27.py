from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dif = 0
        for i in range(len(nums)):
            if nums[i-dif] == val:
                del nums[i-dif]
                dif +=1

        # return len(nums), nums
        return len(nums)

# r = Solution().removeElement([3,2,2,3], 3)
r = Solution().removeElement([0,1,2,2,3,0,4,2], 2)
print(r)
