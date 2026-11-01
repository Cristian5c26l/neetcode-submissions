class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_area = 0
        
        # Time Complexity: O(n)
        # Pattern: Two Pointers

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            max_area = max(max_area, area)
            if heights[L] < heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1
            else:
                L += 1

        return max_area