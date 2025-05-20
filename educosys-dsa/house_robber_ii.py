# https://leetcode.com/problems/house-robber-ii/

class Solution:
    # Max cost of robbing house fron ind to n-1 
    def helper(self, nums: List[int], ind: int, n: int):
        if ind >n: 
            return 0
        inc : int = nums[ind] + self.helper(nums, ind + 2, n)
        exc: int = self.helper(nums, ind + 1, n)
        return max(inc, exc)



    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        #If there's one element then return that itself
        if n == 1:
            return nums[n-1]

        # So the notion of robbing the house if the index is from 0 then it can be robbed to 2nd last
        rob_from_0 = self.helper(nums, 0, n-2)
        # So the notion of robbing the house if the index is from 1 then it can be robbed to last element
        rob_from_1 = self.helper(nums, 1, n-1)

        return max(rob_from_0, rob_from_1)