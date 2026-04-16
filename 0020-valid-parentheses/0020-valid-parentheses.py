class Solution(object):
    def isValid(self, s):
        stack = []

        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0