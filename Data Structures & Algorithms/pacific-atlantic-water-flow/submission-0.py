class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        add all top most and left most to pacific
        pacific -> row 0, col 0
        atlantic -> row ROWS - 1, col COLS - 1

        add all right most and bottom most to 

        dfs on each one
            - if greater than prev -> if yes, add to set

        find intersection of both set
        '''
        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, prev_val, ocean):
            already_checked = (r, c) in ocean
            in_bounds = 0 <= r < ROWS and 0 <= c < COLS

            if already_checked or not in_bounds or not prev_val <= heights[r][c]: # !!!
                return

            ocean.add((r, c))
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)
            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)


        # fixed rows
        for c in range(COLS):
            # pacific
            dfs(0, c, heights[0][c], pacific)
            # atlantic
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)
            
        for r in range(ROWS):
            # pacific
            dfs(r, 0, heights[r][0], pacific)
            # atlantic
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        return [[r, c] for r, c in pacific & atlantic]