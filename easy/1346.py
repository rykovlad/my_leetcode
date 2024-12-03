from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, num1 in enumerate(arr):
            for j, num2 in enumerate(arr):
                if i!=j and (num1*2==num2 or num2*2==num1):
                    return True
        return False

assert Solution().checkIfExist([-2,0,10,-19,4,6,-8]) == False
assert Solution().checkIfExist([2,3,3,0,0]) == True
