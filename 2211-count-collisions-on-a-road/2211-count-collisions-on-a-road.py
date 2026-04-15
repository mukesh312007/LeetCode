class Solution(object):
    def countCollisions(self, directions):
        left = 0
        right = len(directions) - 1
        
        # skip leading L
        while left <= right and directions[left] == 'L':
            left += 1
        
        # skip trailing R
        while left <= right and directions[right] == 'R':
            right -= 1
        
        collisions = 0
        
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1
        
        return collisions