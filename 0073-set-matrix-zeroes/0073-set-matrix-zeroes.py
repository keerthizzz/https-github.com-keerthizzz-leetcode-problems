class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        row_zero, col_zero = set(), set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0



mat1 = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(mat1)
print(mat1)  

mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(mat2)
print(mat2) 
