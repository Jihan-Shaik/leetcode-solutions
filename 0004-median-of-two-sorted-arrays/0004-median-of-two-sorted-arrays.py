class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=list(sorted(nums1+nums2))
        if len(n)%2==0:
            return (n[int((len(n)/2)-1)]+n[int(len(n)/2)])/2
        else:
            return float(n[int((len(n)-1)/2)])
        