class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        left_max = height[0]
        right_max = height[len(height)-1]
        total_water = 0

        while(i<j):

            if height[i] <= height[j]:
                i += 1
                left = height[i]

                if left_max > left:
                    total_water += left_max - left
                else:
                    left_max = left

            elif height[i] > height[j]:
                j -= 1
                right = height[j]
                
                if right_max > right:
                    total_water += right_max - right
                else:
                    right_max = right          

        return total_water



    