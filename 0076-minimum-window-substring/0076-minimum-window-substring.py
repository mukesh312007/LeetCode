class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        from collections import Counter

        need = Counter(t)  
        window = {}

        have, need_count = 0, len(need)
        left = 0
        res = [-1, -1]
        min_len = float('inf')

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                if (right - left + 1) < min_len:
                    res = [left, right]
                    min_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if min_len != float('inf') else ""