class Solution(object):
    def reverseWords(self, s):
        words=""
        S=s.split()
        for i in S[::-1]:
            words+=i+" "
        return words[:-1:]