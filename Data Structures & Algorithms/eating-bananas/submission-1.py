class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while(start <= end):
            mid = start + (end - start) // 2
            counter = 0

            for banana in piles:
                counter += (banana + mid - 1) // mid

            if counter > h:
                start = mid + 1
            elif counter <= h:
                best_speed = mid
                end = mid - 1

        return best_speed


            

