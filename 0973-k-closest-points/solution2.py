import random


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        self._select(points, 0, len(points) - 1, k - 1)
        return points[:k]

    def _select(self, points, lo, hi, target):
        pivot_dist = self._dist(points[random.randint(lo, hi)])
        lt, i, gt = lo, lo, hi

        while i <= gt:
            d = self._dist(points[i])
            if d < pivot_dist:
                points[i], points[lt] = points[lt], points[i]
                lt += 1
                i += 1
            elif d > pivot_dist:
                points[i], points[gt] = points[gt], points[i]
                gt -= 1
            else:
                i += 1

        if target < lt:
            self._select(points, lo, lt - 1, target)
        elif target > gt:
            self._select(points, gt + 1, hi, target)

    def _dist(self, p):
        return p[0] ** 2 + p[1] ** 2

    def test(self):
        print(self.kClosest([[1, 3], [-2, 2]], 1))
        print(self.kClosest([[3, 3], [5, -1], [-2, 4]], 2))


solution = Solution()

solution.test()
