class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target-position) / speed
        cars = zip(position, speed)
        aligned_cars = sorted(cars, reverse = True)
        stk = []

        for p, s in aligned_cars:
            time = (target - p) / s

            if len(stk) == 0 or time > stk[-1]:
                stk.append(time)

        return len(stk)


