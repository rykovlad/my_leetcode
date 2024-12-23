from typing import List


class Solution:
    def most_left_correct_index(self, a, b, h) -> int:
        if a == b:
            return b
        if h[b] > h[a]:
            return b


        left_builds = h[b:]
        set_left = sorted(set(left_builds))
        if set_left[-1] < h[b]:
            return -1


        target_heigt = max(h[b], h[a])
        i = b
        while i < len(h):
            if h[i] > target_heigt:
                return i
            i += 1

        return -1

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans: List[int] = []

        for q in queries:
            a_h, b_h = sorted(q)
            mlci = self.most_left_correct_index(a_h, b_h, heights)
            ans.append(mlci)
        return ans


if __name__ == '__main__':
    s = Solution()
    a = s.most_left_correct_index(0,1, [6,4,8,5,2,7])
    print(a)

if __name__ != '__main__':
    s = Solution()
    a = s.leftmostBuildingQueries([5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]])
    print(a)