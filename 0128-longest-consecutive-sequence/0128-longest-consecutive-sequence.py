class Solution(object):
    def longestConsecutive(self, nums):
        n=sorted(list(set(nums)))
        c=0
        p=[]
        if len(n)==0:
            return 0
        elif len(n)==1:
            return 1
        for i in range(0,len(n)-1):
            if n[i]+1==n[i+1]:
                c+=1
            else:
                p.append(c)
                c=0
            p.append(c)
        return max(p)+1 if p else 0