class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        for i in range(len(s)):
            if (s[i] in seen_s and seen_s[s[i]] != t[i]) or (
                t[i] in seen_t and seen_t[t[i]] != s[i]
            ):
                return False
            seen_s[s[i]] = t[i]
            seen_t[t[i]] = s[i]

        return True

    def test(self):
        print(self.isIsomorphic("egg", "add"))
        print(self.isIsomorphic("f11", "b23"))
        print(self.isIsomorphic("badc", "baba"))


solution = Solution()

solution.test()
