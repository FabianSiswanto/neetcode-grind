class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        parent list
        rank list

        union find -> 2 functions
        - find -> get ancestors till val = par[val]
            do path compression as u go
        - union
            -> if both items' parent same -> do nothing
            -> set item with bigger rank as parent
        '''
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node

            while res != parent[res]:
                # path compression -> updated as it goes
                grandparent = parent[parent[res]]
                parent[res] = grandparent
                
                res = grandparent

            return res


        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0 #nothing happens -> subtract with nothing

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1


        res = n

        for n1, n2 in edges:
            res -= union(n1, n2)

        return res