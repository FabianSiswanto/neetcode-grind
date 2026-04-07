class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        IDEA: q holds rotten oranges, and bfs logic just infects neighbors

        keep track of count of fresh fruits -> fresh_count

        bfs
        -> put all 2s in q
        -> bfs
            -> process items in q
                -> set to 2
                -> if nei valid coor + val is 1 
                    -> set to 2
                    -> add to q
                    -> decrement fresh_count
            -> increment timer

        stop condition -> no 1s -> keep track by set of coordinates?
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        
        fresh_count = 0
        rotten_oranges = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]
                if val == 1:
                    fresh_count += 1
                if val == 2:
                    rotten_oranges.append([r, c])

        timer = 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        while fresh_count > 0 and rotten_oranges: # can just stop if no more fresh oranges
            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()
                grid[r][c] = 2

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    valid_coor = nr in range(ROWS) and nc in range(COLS)
                    if valid_coor and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten_oranges.append([nr, nc])
                        fresh_count -= 1
                
            timer += 1

        return timer if fresh_count == 0 else -1



        