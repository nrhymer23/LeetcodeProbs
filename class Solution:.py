#Code Copied from Leetcode Comments/explantionations added 
#https://leetcode.com/problems/two-sum/


class Solution:
    
    #Fuction creation 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Creation of hash map 
        prevMap = {} # val : index
        
            #checking array(s) index and value 
        for i, n in enumerate(nums):
            diff = target - n
            #checking for value in hashmap
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
    
