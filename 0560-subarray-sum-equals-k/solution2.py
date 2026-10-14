# TODO
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_of_equal = 0
        left = 0
        right = 1

        while left < right:
            sum_subarray = sum(nums[left:right])
            if sum_subarray > k:
                left += 1
            elif sum_subarray < k:
                if right < len(nums):
                    right += 1
                else:
                    left += 1
            else:
                num_of_equal += 1
                left += 1

        return num_of_equal

    def test(self):
        print(self.subarraySum([1, 2, 3], 3))
        print(self.subarraySum([1, 1, 1], 2))


solution = Solution()

solution.test()
