# https://leetcode.com/problems/subsets/

class Solution:
    def helper(self,nums: list[int], ind: int, curr: list[int], res : list[list[int]]) :
        if ind == len(nums):
            res.append(curr.copy())
            return
        # include 
        curr.append(nums[ind])
        self.helper(nums, ind+1, curr, res)
        curr.pop()
        # exclude 
        self.helper(nums, ind+1, curr, res)   

    def subsets(self, nums: list[int]) -> list[list[int]]:
        # We need a array of array 
        res : list[list[int]] = [] # Result array 
        # current array under consideration, 
        curr: list[int] = []
        # start from the front hence the index = 0
        self.helper(nums, 0, curr, res )
        return res
        
