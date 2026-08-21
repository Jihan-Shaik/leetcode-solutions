class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in s[::-1]:
            s.append(i)
        del s[:int(len(s)/2)]