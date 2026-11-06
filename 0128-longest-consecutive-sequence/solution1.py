class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        curr_longest = 0
        for i in range(len(nums)):
            for j in range(len(nums)):


