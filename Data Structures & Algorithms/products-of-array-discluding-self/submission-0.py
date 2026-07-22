class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_list = []
        right_list = [0]*len(nums)
        ans_list = [0]*len(nums)

        left_product = 1
        for i in range(len(nums)):
            left_list.append(left_product)
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            right_list[i] = right_product
            right_product *= nums[i]

        for i in range(len(nums)):
            ans_list[i] = left_list[i] * right_list[i]
            
        return ans_list


        