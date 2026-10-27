class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        for i in coordinates[1::]:
            if (i[1]-coordinates[0][1])*(coordinates[0][0]-coordinates[1][0])!=(coordinates[0][1]-coordinates[1][1])*(i[0]-coordinates[0][0]): return False
        return True