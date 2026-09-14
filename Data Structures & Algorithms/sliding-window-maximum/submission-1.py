from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        i = 0
        j = 0
        output = []

        while(j != len(nums)):

            while q and nums[q[-1]] <= nums[j]:
                q.pop()

            q.append(j)

            if q[0] < i:
                q.popleft()

            if (j - i + 1) == k:
                output.append(nums[q[0]])
                i += 1

            j += 1

        return output

        