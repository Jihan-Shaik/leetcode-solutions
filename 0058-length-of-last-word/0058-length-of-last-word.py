class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        c = 0
        for i in s[::-1]:
            if i != " ":
                c += 1
            else:
                break
        return c