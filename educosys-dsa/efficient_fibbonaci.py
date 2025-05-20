# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        result: int = 0

        if n < 0:
            result = 0
        if n <= 1:
            result = n        
        last = 0
        sec_last = 1
        # 
        for i in range(2, n+1):
            # i = 2,  sec_last = 1, last = 0, result = 1
            # i = 3,  sec_last = 2, last = 1, result = 2
            # i = 4,  sec_last = 2, last = 2, result = 3
            result = last + sec_last # i=3, result = 2 
            last = sec_last 
            sec_last = result
        return result 