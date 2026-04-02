class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        cat -> ca#, c#t, #at
        
        need to be able to find neighbors -> use pattern -> have map from pattern to neighbors
        as traverse -> find nei -> convert word to pattern -> use map to find neighbors
            -> check nei if in visited, if match with endWord
        '''
        res = 0
        patternToWords = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                patternToWords[pattern].append(w)


        def generateNeighbors(word):
            neighbors = []

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                words = patternToWords[pattern]
                neighbors.extend(words)
                
            return neighbors # list of words


        def bfs(beginWord):
            q = deque([[beginWord, 1]])
            visited = set([beginWord])

            while q:
                word, steps = q.popleft()

                for nei in generateNeighbors(word):
                    if nei in visited:
                        continue

                    if nei == endWord:
                        return steps + 1

                    visited.add(nei)
                    q.append([nei, steps + 1])

            return 0
                    
        return bfs(beginWord)