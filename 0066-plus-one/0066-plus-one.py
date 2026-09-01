class Solution(object):
    def plusOne(self, digits):
        a = ""
        for i in digits:
            a += str(i)
        b = int(a) + 1
        c = []
        for i in str(b):
            c.append(int(i))
        return c
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        