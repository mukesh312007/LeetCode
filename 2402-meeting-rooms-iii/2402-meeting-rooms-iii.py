import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort()
        
        free_rooms = list(range(n))  
        heapq.heapify(free_rooms)
        
        busy = []
        count = [0] * n
        
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)
            
            duration = end - start
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))
            
            count[room] += 1
        
        return count.index(max(count))