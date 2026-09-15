class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        # self.min_stk.append(min(self.min_stk[-1], val) if self.min_stk else val)

        if len(self.min_stk) == 0:
            self.min_stk.append(val)
        elif self.min_stk[-1] <= val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        
    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.min_stk[-1]
        
