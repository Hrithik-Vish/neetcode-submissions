class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)

        stk = []
        
        for i in range((len(temperatures)-1), -1, -1):

            if len(stk) == 0:
                stk.append(i)
                continue
            elif temperatures[stk[-1]] <= temperatures[i]:
                while stk and temperatures[stk[-1]] <= temperatures[i]:
                    stk.pop()
                stk.append(i)
            else:
                stk.append(i)
            if len(stk) >= 2: output[i] = stk[-2] - stk[-1]
        return output
            
