class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        j =len(nums)-1
        c = 0
        while(i<j):
            s = nums[i]+nums[j]
            if(s == k):
                i+=1
                j-=1
                c+=1
            elif(s < k):
                i+=1
            else:
                j-=1
        return c
    
    #https://leetcode.com/problems/max-number-of-k-sum-pairs/
