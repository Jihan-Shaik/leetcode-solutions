class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        K=[]
        for i in set(nums): K.append([nums.count(i),i])
        if k<len(K): return [x[1] for x in sorted(K)[-1:-k-1:-1]]
        else: return [x[1] for x in K]