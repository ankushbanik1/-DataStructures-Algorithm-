class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        m=M
        a=sorted(A)
        
        n=len(A)
        
        if (n<m):
            return -1
            
        mindiff=a[n-1]-a[0]    
        
        for i in range(n-M+1):
            mindiff=min(mindiff,a[i+M-1]-a[i])
        return mindiff    
