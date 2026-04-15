class Solution(object):
    def countPalindromicSubsequence(self, s):
        result = 0
        
        for ch in set(s):
            left = s.find(ch)
            right = s.rfind(ch)
            
            if right - left > 1:
                middle = set(s[left + 1:right])
                result += len(middle)
        
        return result