class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                forward = (i - startIndex + n) % n
                backward = (startIndex - i + n) % n
                min_dist = min(min_dist, forward, backward)
        
        return min_dist if min_dist != float('inf') else -1