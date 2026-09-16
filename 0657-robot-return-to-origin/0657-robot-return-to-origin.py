class Solution:
    def judgeCircle(self, moves: str) -> bool:
        L=[0,0]
        for i in moves:
            if i=="U": L[0]+=1
            elif i=="D": L[0]-=1
            elif i=="R": L[1]+=1
            else: L[1]-=1
        return True if L==[0,0] else False