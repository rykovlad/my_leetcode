from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box_count = len(boxes)
        result = [0 for _ in range(box_count)]
        balls = 0
        steps = 0
        for i, box in enumerate(boxes):
            steps = balls + steps
            result[i] = steps
            if box == "1":
                balls += 1

        balls = 0
        steps = 0
        for i in range(box_count-1, -1, -1):
            steps = balls + steps
            result[i] += steps
            if boxes[i] == "1":
                balls += 1

        return result

s = Solution()
print(s.minOperations("0011110"))
