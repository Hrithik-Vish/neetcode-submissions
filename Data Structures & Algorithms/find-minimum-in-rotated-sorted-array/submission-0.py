class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        smallest = nums[0]

        if nums[start] <  nums[end]:
            smallest = nums[start]
            return smallest
            
        while(start <= end):
            mid = start + (end - start) // 2

            if nums[mid] <= nums[end]:
                smallest = min(smallest, nums[mid])
                end = mid -1
                
            else:
                start = mid +1


        return smallest