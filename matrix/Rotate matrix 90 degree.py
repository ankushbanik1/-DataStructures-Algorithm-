class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(0,len(matrix)):
              for col in range(row,len(matrix[0])):
                    
                    matrix[col][row] , matrix[row][col] = matrix[row][col] , matrix[col][row]
            #reverse the matrix  
        for row in matrix:
            
            row.reverse()
