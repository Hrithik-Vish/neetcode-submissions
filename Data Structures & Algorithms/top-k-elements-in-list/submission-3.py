from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        ans = []

        for num in nums_dict:
            bucket[nums_dict[num]].append(num)

        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                if len(ans) != k:
                    ans.append(j)

        return ans



                   