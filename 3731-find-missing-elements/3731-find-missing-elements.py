class Solution(object):
    def findMissingElements(self, nums):
        a, z = min(nums), max(nums)
        L, l = [], []
        for i in range(a,z+1):
            L.append(i)
        for j in L:
            if j not in nums:
                l.append(j)
        return l