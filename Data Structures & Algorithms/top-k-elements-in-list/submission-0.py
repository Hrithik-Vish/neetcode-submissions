class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for value in nums:
            nums_dict[value] = nums_dict.get(value, 0) +1

        buckets = [[] for _ in range(len(nums) +1)]

        for num in nums_dict:
            buckets[nums_dict[num]].append(num)

        ans = []
        
        for value in range(len(buckets)-1, 0, -1):
            for num in buckets[value]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                   