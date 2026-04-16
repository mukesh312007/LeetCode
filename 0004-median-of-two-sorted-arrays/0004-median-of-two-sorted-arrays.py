class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)

        if m > n:
            A, B, m, n = B, A, n, m

        low, high = 0, m
        half = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2   # partition A
            j = half - i            # partition B

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # correct partition found
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1