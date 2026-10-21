class Solution:
    def completePrime(self, num: int) -> bool:
        def prime(n):
            if n<2: return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0: return False
            return True
        a=str(num)
        for i in range(len(a)):
            if not prime(int(a[:i+1:])) or not prime(int(a[-1:-i-2:-1][::-1])): return False
        return True