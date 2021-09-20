#User function Template for python3

class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        
        arr1[:]=sorted(arr1+arr2)
        arr2.clear()
                
