class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U,D,R,L,p=moves.count("U"),moves.count("D"),moves.count("R"),moves.count("L"),[0,0]
        p[0],p[1]=U-D,R-L
        return True if p==[0,0] else False