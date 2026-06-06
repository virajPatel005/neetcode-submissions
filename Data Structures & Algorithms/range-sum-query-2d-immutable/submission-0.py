class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix_matrix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                self.prefix_matrix[i][j] = (
                    matrix[i][j]
                    + (self.prefix_matrix[i - 1][j] if i > 0 else 0)
                    + (self.prefix_matrix[i][j - 1] if j > 0 else 0)
                    - (self.prefix_matrix[i - 1][j - 1] if i > 0 and j > 0 else 0)
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 == 0 and col1 == 0:
            return self.prefix_matrix[row2][col2]

        elif row1 == 0:
            return (
                self.prefix_matrix[row2][col2]
                - self.prefix_matrix[row2][col1 - 1]
            )

        elif col1 == 0:
            return (
                self.prefix_matrix[row2][col2]
                - self.prefix_matrix[row1 - 1][col2]
            )

        return (
            self.prefix_matrix[row2][col2]
            - self.prefix_matrix[row1 - 1][col2]
            - self.prefix_matrix[row2][col1 - 1]
            + self.prefix_matrix[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)