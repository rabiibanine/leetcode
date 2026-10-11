import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        get_distance = lambda point: math.sqrt(point[0] ** 2 + point[1] ** 2)
        k_closest = []

        for _ in range(k):
            current_closest_index = 0

            for i, point in enumerate(points):
                current_closest = points[current_closest_index]
                if get_distance(point) < get_distance(current_closest):
                    current_closest_index = i

            k_closest.append(points.pop(current_closest_index))

        return k_closest

    def test(self):
        print(self.kClosest([[1, 3], [-2, 2]], 1))
        print(self.kClosest([[3, 3], [5, -1], [-2, 4]], 2))


solution = Solution()

solution.test()
