class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        import statistics
        N=[x for x in nums if x%2==0]
        return statistics.mode(sorted(N)) if N else -1