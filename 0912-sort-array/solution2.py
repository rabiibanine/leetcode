import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self._sort(nums, 0, len(nums) - 1)
        return nums

    def _sort(self, nums, lo, hi):
        if lo >= hi:
            return

        pivot = nums[random.randint(lo, hi)]
        left, mid, right = lo, lo, hi

        while mid <= right:
            if nums[mid] < pivot:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] > pivot:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:
                mid += 1

        self._sort(nums, lo, left - 1)
        self._sort(nums, mid + 1, hi)

    def test(self):
        print(self.sortArray([2, 3, 5, 6, 2, 4, 6, 3]))


solution = Solution()

solution.test()
