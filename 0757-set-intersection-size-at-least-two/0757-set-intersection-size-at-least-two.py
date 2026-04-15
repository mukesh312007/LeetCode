class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        a = -1  # second last picked
        b = -1  # last picked
        count = 0
        
        for start, end in intervals:
            if start <= a:
                # already have at least 2 points
                continue
            elif start > b:
                # need to add 2 points
                count += 2
                a = end - 1
                b = end
            else:
                # need to add 1 point
                count += 1
                a = b
                b = end
        
        return count