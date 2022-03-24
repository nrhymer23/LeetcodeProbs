class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window solution 
        
        res = nums[0]
        sum  = 0
        
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            res = max(res, sum)
        return res