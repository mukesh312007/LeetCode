class Solution(object):
    def countMentions(self, numberOfUsers, events):
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        back_time = [0] * numberOfUsers
        
        for typ, time_str, data in events:
            t = int(time_str)
            
            for i in range(numberOfUsers):
                if not online[i] and back_time[i] <= t:
                    online[i] = True
            
            if typ == "OFFLINE":
                user = int(data)
                online[user] = False
                back_time[user] = t + 60
            
            else:  # MESSAGE
                if data == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                
                else:
                    for token in data.split():
                        user = int(token[2:])
                        mentions[user] += 1
        
        return mentions