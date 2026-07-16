class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1.0
        
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive binary exponentiation
        half = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x