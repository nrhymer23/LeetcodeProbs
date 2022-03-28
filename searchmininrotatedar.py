#binary serarch .. you always have p1, p2, & mid + p1 , <= p2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1,p2 = 0, len(nums)-1 
        
        while p1 <= p2:
            mid = (p1 + p2) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion 
            if nums[p1] <= nums[mid]:
                if target > nums[mid] or target < nums[p1]:
                    p1 = mid + 1
                else:
                    p2 = mid - 1
            # right sorted portion 
            else:
                if target < nums[mid] or target > nums[p2]:
                    p2 = mid - 1
                else:
                    p1 = mid + 1
                    
            return -1
         
