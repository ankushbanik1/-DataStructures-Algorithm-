class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        col = []
        
        for i in range(len(matrix)):
            flag = False
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    flag = True
                    if j not in col:
                        col.append(j)
            if flag:
                matrix[i] = [0 for _ in range(len(matrix[0]))]


        for each in col:
            for i in range(len(matrix)):
                matrix[i][each] = 0

                
