class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        n1,n2=num1.partition("+"),num2.partition("+")
        A=str(int(n1[0])*int(n2[0])-int(n1[-1][:-1:])*int(n2[-1][:-1:]))+"+"
        B=str(int(n1[0])*int(n2[-1][:-1:])+int(n2[0])*int(n1[-1][:-1:]))+"i"
        return A+B