class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a,b=0,0
        for i in set(nums1)&set(nums2): a+=nums1.count(i)
        for i in set(nums1)&set(nums2): b+=nums2.count(i)
        return [a,b]