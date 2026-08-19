class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=list(set(nums1)-set(nums2))
        n2=list(set(nums2)-set(nums1))
        return [n1,n2]