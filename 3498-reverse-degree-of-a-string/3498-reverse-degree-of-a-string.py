class Solution:
    def reverseDegree(self, s: str) -> int:
        x=[a for a in range(26,0,-1)]
        y="abcdefghijklmnopqrstuvwxyz"
        c=0
        for i in range(len(s)): c+=x[y.index(s[i])]*(i+1)
        return c