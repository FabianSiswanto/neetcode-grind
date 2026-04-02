class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        actions:
        - if match -> cut word
        - else -> dfs to neighbors -> keep track of visited


        '''
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, word):
            if not word:
                return True

            in_bounds = r in range(ROWS) and c in range(COLS)
            already_visited = (r, c) in visited
            if not in_bounds or already_visited or board[r][c] != word[0]:
                return False

            visited.add((r, c))

            found = (
                dfs(r + 1, c, word[1:]) or
                dfs(r, c + 1, word[1:]) or
                dfs(r - 1, c, word[1:]) or
                dfs(r, c - 1, word[1:])
            )

            visited.remove((r, c)) # backtrack

            return found

            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, word):
                    return True
        
        return False
            
        