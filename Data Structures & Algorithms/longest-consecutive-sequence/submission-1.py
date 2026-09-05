class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        counter_final = 0
        for num in set_nums:
            if (num - 1) not in set_nums:
                value = num
                counter_second = 1
                while ((value+1) in set_nums):
                    counter_second += 1
                    value += 1
                if counter_final < counter_second:
                    counter_final = counter_second
        
        return counter_final
        
