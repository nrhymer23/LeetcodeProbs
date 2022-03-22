
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mathar = [1] * (len(nums))

        prefix = 1 
        for i in range(len(nums)):
             mathar[i]=prefix
             prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
                mathar*=postfix
                postfix*=num[i]
        return mathar
    
    
         # Create an array that will return        
        ret = [1] * len(nums)
        # Store the cumulative product
        cumprod = 1
        
        # Iterate over nums
        for i in range(len(nums)):
            ret[i] = cumprod
            cumprod = nums[i] * cumprod
            
        cumprod = 1
            
        for i in range(len(nums) -1, -1, -1):
            ret[i] *= cumprod
            cumprod = nums[i] * cumprod
            
        return ret