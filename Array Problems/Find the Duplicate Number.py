class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first=second=nums[0]
        
        
        while True:
            
            first=nums[first]
            second=nums[nums[second]]
            
            if first==second:
                break
        first=nums[0]
                    
        while first!=second:
            
            first=nums[first]
            second=nums[second]
            
        return second    
