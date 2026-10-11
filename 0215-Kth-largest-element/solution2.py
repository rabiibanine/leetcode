import random


class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        lo, hi = 0, len(nums) - 1

        while True:
            pivot = nums[random.randint(lo, hi)]
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                hi = lt - 1
            elif target > gt:
                lo = gt + 1
            else:
                return pivot

    def test(self):
        # print(self.findKthLargest([1, 2, 3], 1))
        # print(self.findKthLargest([1, 2, 3], 2))
        # print(self.findKthLargest([2, 2, 3], 3))
        # print(self.findKthLargest([1, 2, 2, 3], 4))

        print(self.findKthLargest([3, 4, 2, 6, 4], 1))


solution = Solution()

solution.test()
