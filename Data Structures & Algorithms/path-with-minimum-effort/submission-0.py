class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        effort = max of |cur - prev val| throughout path -> minimize this

        dijkstra -> take step with the min abs diff 
            -> use min heap for that (abs diff, r, c)

        (visited? target? do others)
        - visited check and update
        - check if r, c is destination
        - check all directions -> if valid and not in visited, add to heap
        '''
        ROWS = len(heights)
        COLS = len(heights[0])

        minHeap = [(0, 0, 0)]
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff # will guaranteed to hit
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                valid_dir = 0 <= nr <= ROWS - 1 and 0 <= nc <= COLS - 1
                if not valid_dir or (nr, nc) in visited:
                    continue

                cur_diff = abs(heights[r][c] - heights[nr][nc])
                new_diff = max(diff, cur_diff)
                item = (new_diff, nr, nc)
                
                heapq.heappush(minHeap, item)




            

        