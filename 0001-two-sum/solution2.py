class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target - num]]
            seen[num] = i

    def test(self):
        array = [2, 7, 11, 15]
        print(self.twoSum(array, 9))


solution = Solution()

solution.test()
