class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        from collections import defaultdict, deque
        
        meetings.sort(key=lambda x: x[2])
        
        know = set([0, firstPerson])
        
        i = 0
        m = len(meetings)
        
        while i < m:
            time = meetings[i][2]
            
            
            graph = defaultdict(list)
            people = set()
            
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1
            
            queue = deque()
            visited = set()
            
            for p in people:
                if p in know:
                    queue.append(p)
                    visited.add(p)
            
            while queue:
                u = queue.popleft()
                know.add(u)
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
        
        return list(know)