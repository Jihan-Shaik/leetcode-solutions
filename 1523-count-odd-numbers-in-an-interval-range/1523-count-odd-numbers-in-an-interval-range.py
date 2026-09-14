class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n=high-low+1
        if n%2==0: return int(n/2)
        elif low%2==0 and high%2==0: return int((n-1)/2)
        elif low%2!=0 and high%2!=0: return int((n+1)/2)