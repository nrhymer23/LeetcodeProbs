from turtle import reset


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force 
    ##     res = 0 
    ##     
    ##     for l in range(len(height)):
    ##         for r in range(l + 1, len(height)):
    ##             area = (r-1) * min = (height[l],height[r])
    ##             res = max (res, area)
    ##             
    ## return res
    
    
    #linear time solution
        res = 0
        l,r = 0, len(height) - 1
        
        while l < r:
            area = (r - 1) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
               l += 1
            else:
                r -= 1
                
        return res