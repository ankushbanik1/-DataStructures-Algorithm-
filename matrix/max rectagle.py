class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        
        n, m = len(matrix), len(matrix[0])
        heights = [0] * (m + 1)
        res = 0
        
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for j in range(m+1):
                while heights[stack[-1]] > heights[j]:
                    prev_height = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    res = max(res, width * prev_height)
                stack.append(j)
        
        return res
