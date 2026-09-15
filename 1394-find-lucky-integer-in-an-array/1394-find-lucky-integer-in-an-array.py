class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=-1
        for i in set(arr): 
            if arr.count(i)==i: a=max(i,a)
        return a