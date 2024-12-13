from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        l = len(nums)
        underscore = [0 for _ in range(l)]
        m = max(nums) + 1
        su = 0

        while su < len(underscore):
            print(nums, "\n", underscore, "\n")
            mmin = m
            t_i = None
            for i, x in enumerate(nums):
                if underscore[i]:
                    continue
                if x < mmin:
                    mmin = x
                    t_i = i

            score += mmin


            if t_i - 1 >= 0:
                su += 1
                underscore[t_i - 1] = 1
            if t_i + 1 < len(underscore):
                su += 1
                underscore[t_i + 1] = 1
            del underscore[t_i]
            del nums[t_i]

        return score



s = Solution()
assert s.findScore([2,1,3,4,5,2]) == 7
assert s.findScore([2,3,5,1,3,2]) == 5
a = s.findScore([46,21,7,33])
print(a)

# this boolshit cant pass time limit, so lets steel that solution:
def findScore(self, nums: List[int]) -> int:
    nums.append(float("inf"))
    res = 0
    start = -1
    i = 1
    while i < len(nums):
        if nums[i] >= nums[i - 1]:
            for j in range(i - 1, start, -2):
                res += nums[j]
            start = i
            i += 1
        i += 1
    return res
