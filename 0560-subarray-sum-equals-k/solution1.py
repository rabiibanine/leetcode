class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_of_equal = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr_sum = sum(nums[i : j + 1])
                if curr_sum == k:
                    num_of_equal += 1

        return num_of_equal

    def test(self):
        print(self.subarraySum([1, 2, 3], 3))
        print(self.subarraySum([1, 1, 1], 2))


solution = Solution()

solution.test()
