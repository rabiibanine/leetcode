class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

    def test(self):
        print(self.isIsomorphic("egg", "add"))
        print(self.isIsomorphic("f11", "b23"))
        print(self.isIsomorphic("badc", "baba"))


solution = Solution()

solution.test()
