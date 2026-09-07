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
                if max_water > water: water = max_water
                i += 1
            else:
                if max_water > water: water = max_water
                j -= 1

        return water

