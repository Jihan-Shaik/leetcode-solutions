class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        c=abs(hour+minutes/60-minutes/5)
        return c*30 if c<=6 else (12-c)*30