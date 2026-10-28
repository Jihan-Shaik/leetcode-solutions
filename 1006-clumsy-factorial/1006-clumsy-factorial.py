class Solution:
    def clumsy(self, n: int) -> int:
        c,s,o="",[str(a) for a in range(n,0,-1)],["*","//","+","-"]
        for i in range(n): c+=s[i]+o[i%4]
        return eval(c[:-2]) if c[-2:]=="//" else eval(c[:-1])