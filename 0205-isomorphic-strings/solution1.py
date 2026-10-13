class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        for i in range(len(s)):
            if (s[i] in seen and seen[s[i]] != t[i]) or (
                t[i] in seen.values() and s[i] not in seen
            ):
                return False
            seen[s[i]] = t[i]
        return True

    def test(self):
        print(self.isIsomorphic("egg", "add"))
        print(self.isIsomorphic("f11", "b23"))
        print(self.isIsomorphic("badc", "baba"))


solution = Solution()

solution.test()
