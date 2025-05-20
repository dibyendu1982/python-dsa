class Solution:
    def climbStairs(self, n: int) -> int:
        # base condition
        if n <= 2 : 
            return n
        return self.climbStairs(n-1) +  self.climbStairs(n-2)