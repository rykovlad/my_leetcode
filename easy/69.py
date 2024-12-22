

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # The square root of 0 or 1 is the number itself

        low, high = 0, x // 2 + 1
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                result = mid  # Update the result because mid might be the answer
                low = mid + 1
            else:
                high = mid - 1

        return result


print(Solution().mySqrt(8))