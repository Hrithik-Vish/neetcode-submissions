class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        smallest = 0

        while(start <= end):
            mid = start + (end - start) // 2

            if nums[mid] <= nums[end]:
                if nums[smallest] > nums[mid]:
                    smallest = mid
                end = mid - 1
            else:
                start = mid + 1
        if nums[0] < nums[-1]:
            start = 0
            end = len(nums) - 1
        elif target <= nums[-1]:
            start = smallest
            end = len(nums) - 1
        else:
            start = 0
            end = smallest - 1

        while(start <= end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid +1        
            else:
                end = mid -1


        return -1