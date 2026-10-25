class Solution:
    def passwordStrength(self, password: str) -> int:
        a,p=0,"".join(set(password))
        for i in p:
            if i.islower(): a+=1
            elif i.isupper(): a+=2
            elif i.isdigit(): a+=3
            elif i in "!@#$": a+=5
        return a