class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums[:-1])):
            c=0
            for j in range(len(nums[i+1:])):
                c+=1
                if nums[i]+nums[i+c]==target: 
                    return [i,i+c]