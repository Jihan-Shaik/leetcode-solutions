class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.istitle() or word.isupper() or word.islower(): return True
        else: return False