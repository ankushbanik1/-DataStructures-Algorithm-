class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        
        count=0
        
        for i in range(0,len(arr-1)):
            if arr[i]+arr[i+1]==k:
                count+=1
                
        return count        
      
      #https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
                
