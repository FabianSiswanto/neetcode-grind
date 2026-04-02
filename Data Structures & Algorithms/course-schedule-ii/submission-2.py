class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        - node: course
        - edge: prereq
            [0, 1]
            0 <- 1 means 1 is a prereq of 0
            1 -> 0

        - not possible to finish all courses -> loop -> len(res) == numCourses

        res = [] -> list of courses in order
        where to start? -> try all from 0 to numCourses

        go over all start of prerequisites
        '''
        prereqs = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        cycle = set()
        visited = set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            # all prereqs already fulfilled
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
        