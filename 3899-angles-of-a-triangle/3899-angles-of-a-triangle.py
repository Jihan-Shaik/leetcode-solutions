class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        import math
        a,b,c=sides[0],sides[1],sides[2]
        if a+b>c and b+c>a and a+c>b:
            return sorted([math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))])
        else: return []