class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        sum=a[0]
        max=0
        
       
        
        for i in range(0,size):
            max=max+a[i]
            
            if sum < max:
                sum=max
            if max<0:
                max=0
        return sum        
            
