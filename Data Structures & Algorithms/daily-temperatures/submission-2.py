class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stk = []
        
        for i in range((len(temperatures)-1), -1, -1):

            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
        
            if stk: output[i] = stk[-1] - i
        
            stk.append(i)
        
        return output
            
