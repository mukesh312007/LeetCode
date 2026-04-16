class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        idx = 0
        direction = -1  

        for ch in s:
            rows[idx] += ch

            if idx == 0 or idx == numRows - 1:
                direction *= -1

            idx += direction

        return "".join(rows)