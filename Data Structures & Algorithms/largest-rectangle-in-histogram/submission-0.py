class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = 0
        right = 0
        stk = []
        max_area = 0
        i = 0

        while(i != len(heights)):

            while stk and (heights[stk[-1]] > heights[i]):
                element = stk.pop()
                if stk:
                    left = stk[-1]
                    right = i
                    area = heights[element] * (right - left - 1)
                else:
                    area = heights[element] * (i)

                if area > max_area:
                    max_area = area
                    
            stk.append(i)
            i += 1

        while stk:
            element = stk.pop()
            if stk:
                left = stk[-1]
                right = len(heights)
                area = heights[element] * (right - left - 1)
            else:
                left = -1
                right = len(heights)
                area = heights[element] * (right - left - 1)
            
            if area > max_area:
                max_area = area

        return max_area




        