class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        tmax, tmin = 1,1
        
        for n in nums:
            if n == 0:
                tmin, tmax = 1,1
                continue
            
            temp = tmax * n 
            tmax = max(n * tmax, n * tmin, n)
            tmin = min(temp, n * tmin, n)
            res = max(res, tmax)
        return res
    
    