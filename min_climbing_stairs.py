# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    # top down - i value is going to go from n-1 to 0
    # bottom up- i value is going to from 0 to n-1 
    # subproblem - determin the cost of climbing stairs from where to where 
    # cost of climbing from index to n-1 
    # cost of climbing from 0 to index 
    # finding cost of climbing from ind to n-1 
    def helper(self, cost: List[int], ind: int):
        if ind >= len(cost):
            return 0

        # this function assumes that you are the stair ind 
        # from there one could go either 1 or 2 steps 
        a = self.helper(cost, ind + 1) # taking 1 step 
        b = self.helper(cost, ind + 2) # taking 2 steps
        # also consider the cost of being at step ind 
        c = cost[ind]
        # return the sum of minimum of both and cost of being at index
        return c + min(a, b)
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Apply pick don't pick 
        # Since the problem states that we can either start from 0 or 1 
        # So we end up starting from both and picking up with minimum of either 
        return min(self.helper(cost, 0), self.helper(cost, 1))
