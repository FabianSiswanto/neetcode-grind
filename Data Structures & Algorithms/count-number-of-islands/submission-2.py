class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        if find 1, do dfs to find all part island (mark other 1s in island as 0)

        dfs:
        - base case: if val is 0, if coord out of bounds not (0<=r<rows, 0<=c<cols)
        - recursive case:
            mark current as visited -> change val to 0
            dfs on all neighbors
        '''

        islands = 0

        def dfs(r, c):
            in_bounds = r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
            if not in_bounds or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

        