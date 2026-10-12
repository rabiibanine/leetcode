class Solution:
    PRIMES = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
    ]

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for s in strs:
            key = self._get_letter_product(s)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())

    def _get_letter_product(self, s: str) -> int:
        product = 1
        for ch in s:
            product *= self.PRIMES[ord(ch) - 97]
        return product

    def test(self):
        print(self.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


solution = Solution()

solution.test()
