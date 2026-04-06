class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        a/c -> a/x * x/c or a/x * x/y * y/c -> just care about from and to
        graph:
        - node: variable
        - edge: from/to's value -> weight

        adjacency list:
        - source: [(to, weight), ...]

        dfs(cur, target, visited, res):
        - if cur is target -. return 1
        - when going over neighbors -> make sure u dont revisit -> prevent cycle
        '''
        graph = defaultdict(list)

        for i, eq in enumerate(equations):
            source, to = eq
            weight = values[i]

            graph[source].append([to, weight])
            graph[to].append([source, 1 / weight])

        def dfs(source: str, target: str, visited: set) -> int:
            if source not in graph or target not in graph:
                return -1

            if source == target:
                return 1

            visited.add(source)

            neighbors = graph[source]
            for to, weight in neighbors:
                if to in visited:
                    continue
                res = dfs(to, target, visited) #TODO: UNDERSTAND THIS
                # try to find valid one
                if res != -1:
                    return weight * res
            
            return -1

        return [dfs(source, target, set()) for source, target in queries]
                

            