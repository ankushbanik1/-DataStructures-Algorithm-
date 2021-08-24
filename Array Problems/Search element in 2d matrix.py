class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n=len(matrix)
        
        m=len(matrix[0])
        
        if n<=0:
            return false
        
        hi=(n*m)-1
        low=0
        
        while (low<=hi):
            mid=(low+(hi-low)//2)
            
            
            if matrix[mid//m][mid%m]==target:
                return True
            elif matrix[mid//m][mid%m]<target:
                low=mid+1
            else:
                
                hi=mid-1
                
                
        return False        
                
