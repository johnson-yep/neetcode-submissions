class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        l, r = 0, n-1

        while l<r:
            best = max(best, min(heights[l], heights[r]) * (r-l))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return best