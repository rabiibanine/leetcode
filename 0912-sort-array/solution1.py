import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        pivot_index = random.randint(0, len(nums) - 1)
        pivot = nums[pivot_index]
        nums[0], nums[pivot_index] = nums[pivot_index], nums[0]
        smaller = []
        bigger = []

        for num in nums[1:]:
            if num >= pivot:
                bigger.append(num)
            else:
                smaller.append(num)

        return self.sortArray(smaller) + [pivot] + self.sortArray(bigger)

    def test(self):
        print(self.sortArray([2, 3, 5, 6, 2, 4, 6, 3]))


solution = Solution()

solution.test()
