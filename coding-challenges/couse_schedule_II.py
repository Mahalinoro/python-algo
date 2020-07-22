# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example:
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .

from collections import defaultdict, deque

class Solution:
    class Graph:
        def __init__(self, vertices):
            self.graph = defaultdict(list)
            
        def addEdge(self, u, v):
            self.graph[u].append(v)
        
    def initGraph(self, prerequisites):
        g = self.Graph(0)
        
        for l in range(len(prerequisites)):
            g.addEdge(prerequisites[l][1], prerequisites[l][0])  

        return g.graph
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = self.initGraph(prerequisites)
        
        indegree = {}
        for dest, src in prerequisites:
            indegree[dest] = indegree.get(dest, 0) + 1

        indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        courses = []

        while indegree_queue:
            vertex = indegree_queue.popleft()
            courses.append(vertex)

            if vertex in g:
                for neighbor in g[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        indegree_queue.append(neighbor)
        
        
        return courses if len(courses) == numCourses else []