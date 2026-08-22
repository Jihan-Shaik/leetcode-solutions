class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        N=[]
        for i in range(n):
            N.append(nums[i])
            N.append(nums[i+n])
        return N