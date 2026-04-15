class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)
        
        while i < n - 1:
            if bits[i] == 1:
                i += 2  # two-bit character
            else:
                i += 1  # one-bit character
        
        return i == n - 1
        