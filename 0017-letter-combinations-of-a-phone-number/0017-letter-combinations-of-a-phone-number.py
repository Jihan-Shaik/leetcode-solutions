class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        import itertools
        l=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        s=[l[int(a)-2] for a in digits]
        return ["".join(a) for a in itertools.product(*s)]