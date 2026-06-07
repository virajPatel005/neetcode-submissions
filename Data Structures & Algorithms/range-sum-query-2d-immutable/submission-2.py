class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)+1
        col=len(matrix[0])+1
        self.prefix_matrix=[[0 for j in range (col)] for i in range(row)]

        for i in range(1,row):
            sum=0
            for  j in range(1,col):
                if i==1 :
                    sum+=matrix[i-1][j-1]
                    self.prefix_matrix[i][j]=sum
               
                else:
                    self.prefix_matrix[i][j]=matrix[i-1][j-1]+self.prefix_matrix[i-1][j]+self.prefix_matrix[i][j-1]-self.prefix_matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        sum=self.prefix_matrix[row2+1][col2+1]-self.prefix_matrix[row1][col2+1]-self.prefix_matrix[row2+1][col1]+self.prefix_matrix[row1][col1]
        return sum
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)