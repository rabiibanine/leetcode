# TODO
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_of_equal = 0
        seen = {0: 1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            num_of_equal += seen.get(sum - k, 0)
            seen[sum] = seen.get(sum, 0) + 1

        return num_of_equal

    def test(self):
        print(self.subarraySum([1, 2, 3], 3))
        print(self.subarraySum([1, 1, 1], 2))
        print(self.subarraySum([1, -1, 0], 0))
        print(self.subarraySum([1, -1], 0))


solution = Solution()

solution.test()
