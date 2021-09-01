import numpy as np
class Solution:
    def median(self, matrix, r, c):

        
#code here
        x = np.array(matrix)
        y=np.ravel(x)
        z = sorted(y)
        left = 0
        right = len(z)-1
        mid = (left + (right-left))//2
        return(z[mid])
