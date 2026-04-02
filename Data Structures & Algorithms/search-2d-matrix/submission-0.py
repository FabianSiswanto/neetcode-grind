class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        l -> first item in first row
        r -> right item in last row

        convert combined arr i to matrix r, c
        i
        r -> i % ROWS
        '''
        ROWS = len(matrix) #3
        COLS = len(matrix[0]) #4

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2

            row = m // COLS
            col = m % COLS

            if matrix[row][col] > target:
                # go left
                r = m - 1
            elif matrix[row][col] < target:
                # go right
                l = m + 1
            else: # found target
                return True

        return False