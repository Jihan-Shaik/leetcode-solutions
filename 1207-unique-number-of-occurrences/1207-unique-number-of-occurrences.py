class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Arr=[arr.count(a) for a in set(arr)]
        return True if len(Arr)==len(set(Arr)) else False