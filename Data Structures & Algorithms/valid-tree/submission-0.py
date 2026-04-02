class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        tree properties:
        - no cycle -> keep track of visited
            - make sure no false positive of going back to parent -> keep prev
        - everything is connected -> len(visited) == n

        graph is undirected -> direction both ways
        '''
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node, prev) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                # make sure no false positive of going back to parent
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False

            return True


        no_cycle = dfs(0, -1)
        everything_connected = len(visited) == n

        return no_cycle and everything_connected