class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
        if n == 0:
            return 1
        base = x if n>0 else 1/x
        result = base
        
        for _ in range(abs(n)-1):
            result *= base
        
        return result
