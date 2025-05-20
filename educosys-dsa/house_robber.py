# https://leetcode.com/problems/house-robber/

class Solution:

    # amount of robbing from ind to n-1 
    def helper(self, nums: list[int], ind: int):
        if ind >= len(nums):
            return 0 
        # if you decide the rob the index then add the cost of the index and move 2 steps further
        rob_index_cost : int = nums[ind] + self.helper(nums, ind + 2)
        # if don't pick the index no need to add the cost of current and move to next by 1 step
        dont_rob_index_cost: int = self.helper(nums, ind + 1) 

        return max(rob_index_cost , dont_rob_index_cost)

    def rob(self, nums: list[int]) -> int:
        # Start from index 0 
        cost_of_robbing_0 = self.helper(nums, 0)
        return cost_of_robbing_0


