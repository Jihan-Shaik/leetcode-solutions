class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=[]
        for i in points: i.insert(0,(i[0]**2+i[1]**2)**0.5)
        points.sort()
        for j in range(k): d.append(points[j][1::])
        return d