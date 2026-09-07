class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        width = j - i
        height = min(heights[i], heights[j])
        water = width * height
        

        while(i < j):
            width = j - i
            height = min(heights[i], heights[j])
            max_water = width * height

            if heights[i] < heights[j]:
                water = max(max_water, water)
                i += 1
            else:
                water = max(max_water, water)
                j -= 1

        return water

