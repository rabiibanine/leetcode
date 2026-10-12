class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append([s])

        print(groups.values())
        return list(groups.values())

    def test(self):
        print(self.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


solution = Solution()

solution.test()
