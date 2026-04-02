class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        if find 1, do dfs to find all part island (mark other 1s in island as 0)

        dfs:
        - base case: if val is 0, if coord out of bounds not (0<=r<rows, 0<=c<cols)
        - recursive case:
            mark current as visited -> change val to 0
            dfs on all neighbors

        bfs:
        - q
        - while q
        '''

        islands = 0

        # def dfs(r, c):
        #     in_bounds = r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
        #     if not in_bounds or grid[r][c] == "0":
        #         return

        #     grid[r][c] = "0"
        #     dfs(r - 1, c)
        #     dfs(r + 1, c)
        #     dfs(r, c - 1)
        #     dfs(r, c + 1)

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()

                in_bounds = 0 <= row < len(grid) and 0 <= col < len(grid[0])
                if not in_bounds or grid[row][col] == "0":
                    continue
                
                grid[row][col] = "0"
                q.append((row - 1, col))
                q.append((row + 1, col))
                q.append((row, col - 1))
                q.append((row, col + 1))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

        