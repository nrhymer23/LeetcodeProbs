class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #binary search 
        res = nums[0]
        p1, p2 = 0, len(nums)-1
        
        #checking postion of values 
        while p1 <= p2:
            if nums[p1] < nums[p2]:
                res = min(res, nums[p1])
                break
        
        
        #if not sorted... 
            mid = (p1 + p2) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[p1]:
                p1 = mid + 1
            else:
                p2 = mid - 1
        return res