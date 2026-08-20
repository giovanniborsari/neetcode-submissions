class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(heights) - 1
        #left >= right we checked all possibilities
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            max_vol = max(max_vol, w * h)

            #if heights[left] is smaller update left pointer
            if heights[left] < heights[right]:
                left += 1
            #Otherwise update right pointer
            else:
                right -= 1

        return max_vol
